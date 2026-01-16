# Week 5: Data Wrangling and Aggregation — Group Mentor Guide

Welcome to Week 5 of the Python course! This week, students are learning:

- Data selection methods: `.loc[]`, `.iloc[]`, boolean filtering
- Data aggregation with `groupby()` and `agg()`
- Merging DataFrames with `merge()` and different join types
- Data transformation: creating/modifying columns
- Pivot tables with `pd.pivot_table()`

Students are working on Kaggle notebooks this week.

## Warm-Up (5–10 minutes)

Choose one:

**Relationship-Building**
- What's been the most challenging part of working with Pandas so far?
- When you look at a spreadsheet, how do you find specific information?

**Check for Understanding (from last week)**
- What's the difference between a Pandas Series and a DataFrame?
- How do you read a CSV file into a DataFrame?
- What does `df.head()` show you?

## Explore vs. Apply — Session Formats

**Explore Sessions** → Walk through selection, aggregation, and merge examples  
**Apply Sessions** → Debug student code, work through Kaggle assignment challenges

## Sample Timing for 1-Hour Session

| Time      | Activity                             |
|-----------|--------------------------------------|
| 0:00–0:10 | Warm-up + review last week           |
| 0:10–0:30 | Explore: data wrangling fundamentals |
| 0:30–0:50 | Apply: live code + assignment help   |
| 0:50–1:00 | Wrap-up + final questions            |

## Check for Understanding (Ask 2–3)

- What's the difference between `.loc[]` and `.iloc[]`?
- What does `groupby()` actually do to the data?
- What's the difference between an inner join and an outer join?
- When would you use a pivot table vs groupby?
- What does `merge()` return when there's no matching key?

## Explore Prompts

Use these to demonstrate key concepts live:

- Let's explore the four main data selection methods
- How do we aggregate data by groups?
- What happens when we merge two DataFrames with different keys?

*Mini-Demo Ideas:*

```python
import pandas as pd

# Data Selection
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'Score': [85, 92, 88, 76]
})

# .loc[] - label-based
print(df.loc[0:2, ['Name', 'Age']])

# .iloc[] - position-based
print(df.iloc[:2])

# Boolean filtering
print(df[df['Age'] > 24])

# GroupBy aggregation
print(df.groupby('Age').agg({'Score': 'mean'}))
```

## Apply Prompts (Live Coding & Troubleshooting)

### Assignment Hotspots

- Confusing `.loc[]` (label-based) with `.iloc[]` (position-based)
- Forgetting parentheses around boolean conditions with `&` or `|`
- Not understanding merge join types
- String operations need `.str.` prefix

### Try This Live

**Let's walk through merging DataFrames:**

```python
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Score': [85, 92, 88]})

# Inner join
inner = pd.merge(df1, df2, on='ID', how='inner')
print(inner)

# Outer join
outer = pd.merge(df1, df2, on='ID', how='outer')
print(outer)
```

Ask:
- What rows are in the inner join result?
- Why do we have NaN values in the outer join?

## Engagement Strategies (for quiet groups)

- "Can someone predict what this merge will return?"
- "Try breaking the groupby on purpose — what error do we get?"
- "Which join type would you use for this scenario?"

## Optional Challenges

- Create a pivot table showing sales by region and product
- Write a query that finds the top 3 scorers in each age group
- Merge three DataFrames together

✅ Mentor To-Do
- [ ] Run a session using this guide
- [ ] Help students understand merge join types
- [ ] Submit your [Mentor Session Report](https://airtable.com/appoSRJMlXH9KvE6w/shrp0jjRtoMyTXRzh)
