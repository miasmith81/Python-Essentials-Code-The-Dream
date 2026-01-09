#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════════
📊 Week 6: SQL & Databases - Test Database Setup Script
Code the Dream - Python Essentials
═══════════════════════════════════════════════════════════════════════════════

This script creates and initializes the test.db SQLite database from test.sql.
Run this script before starting the Week 6 SQL exercises.

Usage:
    python setup_test_db.py
    
The script will:
    1. Create test.db in the current directory (or recreate if it exists)
    2. Execute all SQL statements from test.sql
    3. Verify the database was created correctly
    4. Print a summary of all tables and row counts

═══════════════════════════════════════════════════════════════════════════════
"""

import sqlite3
import os
from pathlib import Path


def setup_database(sql_file: str = "test.sql", db_file: str = "test.db") -> bool:
    """
    Create and populate the test database from the SQL file.
    
    Args:
        sql_file: Path to the SQL file containing schema and data
        db_file: Path to the SQLite database file to create
        
    Returns:
        True if successful, False otherwise
    """
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    sql_path = script_dir / sql_file
    db_path = script_dir / db_file
    
    print("═" * 70)
    print("📊 Week 6: SQL Database Setup")
    print("═" * 70)
    
    # Check if SQL file exists
    if not sql_path.exists():
        print(f"❌ Error: SQL file not found: {sql_path}")
        return False
    
    # Remove existing database to start fresh
    if db_path.exists():
        print(f"🗑️  Removing existing database: {db_file}")
        os.remove(db_path)
    
    # Read SQL file
    print(f"📖 Reading SQL file: {sql_file}")
    with open(sql_path, "r", encoding="utf-8") as f:
        sql_script = f.read()
    
    # Connect to database and execute SQL
    print(f"🔗 Creating database: {db_file}")
    
    try:
        with sqlite3.connect(db_path) as conn:
            # Enable foreign keys
            conn.execute("PRAGMA foreign_keys = ON")
            
            # Execute the entire SQL script
            conn.executescript(sql_script)
            conn.commit()
            
            print("✅ SQL script executed successfully!")
            print()
            
            # Verify and display table information
            verify_database(conn)
            
        return True
        
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


def verify_database(conn: sqlite3.Connection) -> None:
    """
    Verify the database was created correctly and print summary.
    
    Args:
        conn: Active SQLite database connection
    """
    print("📋 Database Verification")
    print("-" * 70)
    
    # Get list of tables
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name NOT LIKE 'sqlite_%'
        ORDER BY name
    """)
    tables = cursor.fetchall()
    
    if not tables:
        print("⚠️  Warning: No tables found in database!")
        return
    
    print(f"📊 Found {len(tables)} tables:\n")
    
    # Print info for each table
    total_rows = 0
    for (table_name,) in tables:
        # Get row count
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        row_count = cursor.fetchone()[0]
        total_rows += row_count
        
        # Get column info
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        column_names = [col[1] for col in columns]
        
        print(f"  📁 {table_name}")
        print(f"     Rows: {row_count}")
        print(f"     Columns: {', '.join(column_names)}")
        print()
    
    print("-" * 70)
    print(f"✅ Total: {len(tables)} tables, {total_rows} rows")
    print()
    
    # Sample query to verify joins work
    print("🔍 Sample Query Test (Albums with Artists):")
    print("-" * 70)
    cursor.execute("""
        SELECT 
            albums.title AS album,
            artists.name AS artist,
            albums.release_year AS year
        FROM albums
        INNER JOIN artists ON albums.artist_id = artists.artist_id
        ORDER BY albums.release_year
        LIMIT 5
    """)
    results = cursor.fetchall()
    
    print(f"{'Album':<35} {'Artist':<20} {'Year':<6}")
    print("-" * 61)
    for album, artist, year in results:
        print(f"{album:<35} {artist:<20} {year:<6}")
    
    print()
    print("═" * 70)
    print("🎉 Database setup complete! Ready for Week 6 exercises.")
    print("═" * 70)


def main():
    """Main entry point."""
    success = setup_database()
    
    if success:
        print("\n💡 Next steps:")
        print("   1. Open the Week 6 SQL notebook")
        print("   2. Connect to test.db using sqlite3 or pandas")
        print("   3. Practice your SQL queries!")
        print()
    else:
        print("\n⚠️  Setup failed. Please check the error messages above.")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
