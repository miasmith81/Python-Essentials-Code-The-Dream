#!/usr/bin/env python3
"""Fix week8 notebooks to work correctly in Google Colab."""

import json
from pathlib import Path

COLAB_SETUP_CODE = '''# ═══════════════════════════════════════════════════════════════════════════════
# 🚀 SETUP: Create the test database (works in Colab & local Jupyter)
# ═══════════════════════════════════════════════════════════════════════════════

import sqlite3
import os
from pathlib import Path

# Check if we're in Google Colab
try:
    import google.colab
    IN_COLAB = True
    print("☁️  Running in Google Colab - setting up environment...")
    
    # Clone the repo if not already present
    if not os.path.exists('Python-Essentials-Code-The-Dream'):
        !git clone https://github.com/StrayDogSyn/Python-Essentials-Code-The-Dream.git
        print("✅ Repository cloned!")
    
    # Change to week8 directory
    os.chdir('Python-Essentials-Code-The-Dream/notebook-sessions/week8')
    print(f"📁 Working directory: {os.getcwd()}")
    
except ImportError:
    IN_COLAB = False
    print("💻 Running locally")

# Now set up the database
DB_PATH = "test.db"
SQL_PATH = "test.sql"

# Check if SQL file exists
if os.path.exists(SQL_PATH):
    # Remove existing database
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print("🗑️  Removed existing database")
    
    # Read and execute SQL
    with open(SQL_PATH, 'r', encoding='utf-8') as f:
        sql_script = f.read()
    
    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript(sql_script)
        
        # Verify tables
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
        tables = cursor.fetchall()
        
    print("═" * 60)
    print("✅ Database created successfully!")
    print(f"📊 Tables: {', '.join([t[0] for t in tables])}")
    print("═" * 60)
else:
    print("⚠️  SQL file not found. Make sure you're in the week8 directory.")
    print(f"   Looking for: {os.path.abspath(SQL_PATH)}")'''

def fix_notebook(notebook_path):
    """Fix a notebook's setup cell to work in Colab."""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    modified = False
    cells_to_remove = []
    setup_cell_replaced = False
    
    for i, cell in enumerate(nb['cells']):
        if cell.get('cell_type') != 'code':
            continue
            
        source = cell.get('source', [])
        if isinstance(source, list):
            code = ''.join(source)
        else:
            code = source
        
        # Find cell with %run that needs to be replaced
        if '%run setup_test_db.py' in code and 'google.colab' not in code:
            print(f"  Replacing old setup cell at index {i}")
            # Convert the new code to a list of lines
            lines = COLAB_SETUP_CODE.split('\n')
            cell['source'] = [line + '\n' if j < len(lines) - 1 else line 
                              for j, line in enumerate(lines)]
            modified = True
            setup_cell_replaced = True
        
        # Mark duplicate Colab setup cells for removal
        elif 'google.colab' in code and 'SETUP' in code:
            if setup_cell_replaced:
                cells_to_remove.append(i)
                print(f"  Marking duplicate cell at index {i} for removal")
    
    # Remove duplicates (in reverse order to preserve indices)
    for i in reversed(cells_to_remove):
        del nb['cells'][i]
        modified = True
        print(f"  Removed duplicate cell")
    
    if modified:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
        return True
    return False

def main():
    week8_dir = Path("notebook-sessions/week8")
    
    print("=" * 60)
    print("FIXING WEEK 8 NOTEBOOKS FOR GOOGLE COLAB")
    print("=" * 60)
    
    for nb_path in week8_dir.glob("*.ipynb"):
        print(f"\nProcessing: {nb_path.name}")
        if fix_notebook(nb_path):
            print(f"  ✅ Fixed!")
        else:
            print(f"  ⏭️  No changes needed")
    
    print("\n" + "=" * 60)
    print("Done!")
    print("=" * 60)

if __name__ == "__main__":
    main()
