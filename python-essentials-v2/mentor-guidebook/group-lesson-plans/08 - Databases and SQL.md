# Week 8: Databases & SQL — Group Mentor Guide

Welcome to Week 8 of the Python course! This week, students are learning:

- Relational database concepts and why they're used
- Creating and connecting to SQLite databases
- Defining tables with proper schema (primary keys, foreign keys, constraints)
- Writing basic SQL queries (SELECT, INSERT, UPDATE, DELETE)
- Handling one-to-many and many-to-many relationships
- Using JOIN statements to combine tables
- Integrating SQL with Pandas using `pd.read_sql_query()`

Students are building a magazine subscription database with publishers, magazines, subscribers, and subscriptions.

## Warm-Up (5–10 minutes)

Choose one:

**Relationship-Building**
- What subscriptions do you have? (magazines, streaming services, apps)
- Have you ever wondered how a company tracks who's subscribed to what?

**Check for Understanding (from last week)**
- How do you handle missing data in a DataFrame?
- What's a regular expression used for?
- How do you validate data before processing it?

## Explore vs. Apply — Session Formats

**Explore Sessions** → Walk through database concepts, table relationships, and SQL syntax  
**Apply Sessions** → Debug SQL queries, troubleshoot foreign key issues, practice JOINs

## Sample Timing for 1-Hour Session

| Time      | Activity                                       |
|-----------|------------------------------------------------|
| 0:00–0:10 | Warm-up + review database concepts             |
| 0:10–0:30 | Explore: tables, relationships, basic queries  |
| 0:30–0:50 | Apply: write queries, debug joins, test code   |
| 0:50–1:00 | Wrap-up + final questions                      |

## Check for Understanding (Ask 2–3)

- What's the difference between a primary key and a foreign key?
- What are the three types of table relationships?
- Why use a join table for many-to-many relationships?
- What's the difference between `JOIN` and `LEFT JOIN`?
- Why do we use constraints like `NOT NULL` and `UNIQUE`?
- What does `PRAGMA foreign_keys = 1` do?

## Explore Prompts

Use these to demonstrate key concepts live:

- Let's map out the magazine database — what tables do we need?
- Where should foreign keys go in a one-to-many relationship?
- How do we handle many-to-many? Let's draw it.

*Mini-Demo Ideas:*

```python
import sqlite3

# Connect to database
with sqlite3.connect("magazines.db") as conn:
    cursor = conn.cursor()
    
    # Create table with constraints
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
    """)
    
    # Insert with parameterized query (safe!)
    cursor.execute(
        "INSERT INTO publishers (name) VALUES (?)", 
        ("National Geographic",)
    )
    conn.commit()
    
    # Query data
    cursor.execute("SELECT * FROM publishers")
    for row in cursor.fetchall():
        print(row)
```

## Apply Prompts (Live Coding & Troubleshooting)

### Assignment Hotspots
- Forgetting `PRAGMA foreign_keys = 1` — constraints won't work!
- Not committing transactions — changes disappear
- Missing `IF NOT EXISTS` — crashes on second run
- Foreign key points to wrong table or column
- Forgetting the comma in single-element tuples: `(value,)` not `(value)`
- Not handling `sqlite3.IntegrityError` for duplicates

### Try This Live

**Let's figure out the magazine database structure:**

Ask:
- Publishers → Magazines: Is this one-to-many? Which table gets the foreign key?
- Subscribers → Magazines: Is this many-to-many? Do we need a join table?

```python
# Find all magazines for a publisher
cursor.execute("""
    SELECT publishers.name, magazines.name 
    FROM magazines
    JOIN publishers ON magazines.publisher_id = publishers.publisher_id
    WHERE publishers.name = ?
""", ("National Geographic",))

for row in cursor.fetchall():
    print(f"Publisher: {row[0]}, Magazine: {row[1]}")
```

Ask:
- Why do we need the JOIN?
- What if a publisher has no magazines? Would `LEFT JOIN` help?

## Integration with Pandas

```python
import pandas as pd
import sqlite3

with sqlite3.connect("lesson.db") as conn:
    sql = """
        SELECT li.line_item_id, li.quantity, p.product_name, p.price
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id
    """
    df = pd.read_sql_query(sql, conn)
    
    # Now use Pandas to analyze
    df['total'] = df['quantity'] * df['price']
    summary = df.groupby('product_name')['total'].sum()
    print(summary)
```

## Engagement Strategies (for quiet groups)

- **Whiteboard It**: "Let's draw the table relationships"
- **SQL Detective**: "Here's a query that's not working — can you spot the error?"
- **Relationship Quiz**: "I say a scenario, you tell me: one-to-one, one-to-many, or many-to-many?"

## Optional Challenges

- Add a `renewal_date` to subscriptions and query expiring ones
- Write a query to count subscribers per magazine
- Create a function that displays all of a subscriber's magazines

✅ Mentor To-Do
- [ ] Run a session using this guide
- [ ] Help students visualize table relationships (draw diagrams!)
- [ ] Check that students installed SQLite Viewer extension
- [ ] Submit your [Mentor Session Report](https://airtable.com/appoSRJMlXH9KvE6w/shrp0jjRtoMyTXRzh)
