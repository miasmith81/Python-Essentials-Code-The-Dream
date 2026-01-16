# Week 6: Data Cleaning and Validation — Group Mentor Guide

Welcome to Week 6 of the Python course! This week, students are learning:

- Handling missing data with `dropna()` and `fillna()`
- Pivot tables with `pd.pivot_table()`
- The `apply()` method for complex row-by-row logic
- Removing duplicates and handling outliers
- Data standardization and validation

Students are working on Kaggle notebooks with real datasets.

## Warm-Up (5–10 minutes)

Choose one:

**Relationship-Building**
- What's a dataset you've encountered that was messy or incomplete?
- Have you ever had to clean up data manually?

**Check for Understanding (from last week)**
- What's the difference between `.loc[]` and `.iloc[]`?
- How does `groupby()` work?
- What's an inner join vs an outer join?

## Explore vs. Apply — Session Formats

**Explore Sessions** → Walk through data cleaning techniques with examples  
**Apply Sessions** → Debug student code, work through Kaggle assignment

## Sample Timing for 1-Hour Session

| Time      | Activity                                |
|-----------|-----------------------------------------|
| 0:00–0:10 | Warm-up + review last week              |
| 0:10–0:30 | Explore: demonstrate cleaning techniques |
| 0:30–0:50 | Apply: assignment help + live coding    |
| 0:50–1:00 | Wrap-up + final questions               |

## Check for Understanding (Ask 2–3)

- What's the difference between `dropna()` and `fillna()`?
- When would you use median vs mean to fill missing values?
- What does `apply()` with `axis=1` do?
- How is a pivot table different from `groupby()`?
- What does `drop_duplicates()` keep by default?

## Explore Prompts

Use these to demonstrate key concepts live:

- Let's see what happens when we have missing data
- How does `fillna()` work with different strategies?
- When would we use `apply()` instead of operators?

*Mini-Demo Ideas:*

```python
import pandas as pd
import numpy as np

# Missing data example
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', None, 'David'],
    'Age': [25, None, 30, 35]
})

# Find and handle missing data
print(df.info())
print(df.dropna())
print(df.fillna({'Name': 'Unknown', 'Age': df['Age'].mean()}))

# Pivot table
sales = pd.DataFrame({
    'Product': ['Widget', 'Gizmo', 'Widget'],
    'Region': ['North', 'South', 'North'],
    'Revenue': [100, 150, 200]
})
pivot = pd.pivot_table(sales, index='Product', columns='Region', values='Revenue', aggfunc='sum')
print(pivot)

# apply() for complex logic
def categorize_age(row):
    if row['Age'] > 30:
        return 'Senior'
    return 'Junior'

df['Category'] = df.apply(categorize_age, axis=1)
```

## Apply Prompts (Live Coding & Troubleshooting)

### Assignment Hotspots
- Forgetting `axis=1` in `apply()` — processes columns instead of rows
- Using string `'NaN'` instead of `np.nan`
- Confusion between pivot table parameters
- CSV separator issues (some files use `|` instead of `,`)

### Try This Live

**Let's walk through the apply() pattern:**

```python
def calculate_bonus(row):
    if row['Sales'] > 1000:
        return row['Sales'] * 0.1
    return 0

df['Bonus'] = df.apply(calculate_bonus, axis=1)
```

Ask:
- What does `axis=1` mean?
- What's the difference between `apply()` and `map()`?

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| "SettingWithCopyWarning" | Use `.copy()` to create true copies |
| String operations don't work | Check column dtype, use `.str.` prefix |
| NaN comparison fails | Use `pd.isna()` or `.isna()` method |
| apply() returns wrong result | Check `axis` parameter |

## Engagement Strategies (for quiet groups)

- "What would happen if we forgot axis=1?"
- "When would you drop missing data vs fill it?"
- "Can someone explain the pivot table parameters?"

## Optional Challenges

- Create a pivot table with multiple aggregation functions
- Write an `apply()` function that uses multiple columns
- Handle outliers using IQR method

✅ Mentor To-Do
- [ ] Run a session using this guide
- [ ] Help students understand `apply()` with `axis=1`
- [ ] Submit your [Mentor Session Report](https://airtable.com/appoSRJMlXH9KvE6w/shrp0jjRtoMyTXRzh)
