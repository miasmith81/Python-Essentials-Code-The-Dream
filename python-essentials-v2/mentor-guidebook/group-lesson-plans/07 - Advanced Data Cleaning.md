# Week 7: Advanced Data Cleaning with Pandas — Group Mentor Guide

Welcome to Week 7 of the Python course! This week, students are learning:

- Regular expressions for pattern matching
- Advanced string methods with `.str`
- Fuzzy matching with the `thefuzz` library
- `groupby()` with `transform()` for complex cleaning
- Multi-step data cleaning workflows

Students are working on complex data cleaning in Kaggle notebooks.

## Warm-Up (5–10 minutes)

Choose one:

**Relationship-Building**
- What's the messiest dataset you've ever worked with?
- Have you encountered misspelled data entries before?

**Check for Understanding (from last week)**
- What's the difference between `dropna()` and `fillna()`?
- When would you use the `apply()` method?
- How do pivot tables differ from `groupby()`?

## Explore vs. Apply — Session Formats

**Explore Sessions** → Walk through regex and fuzzy matching examples  
**Apply Sessions** → Debug student code, work through regex patterns

## Sample Timing for 1-Hour Session

| Time      | Activity                                |
|-----------|-----------------------------------------|
| 0:00–0:10 | Warm-up + review last week              |
| 0:10–0:30 | Explore: demonstrate regex patterns     |
| 0:30–0:50 | Apply: assignment help + debugging      |
| 0:50–1:00 | Wrap-up + final questions               |

## Check for Understanding (Ask 2–3)

- What is a regular expression used for?
- How does `groupby().transform()` differ from `groupby().agg()`?
- What does `.str.extract()` return?
- When would you use fuzzy matching vs exact matching?
- What does `mode()` return for a group?

## Explore Prompts

Use these to demonstrate key concepts live:

- Let's match phone numbers with a regex pattern
- How do we correct spelling variations?
- What's the difference between `transform()` and `agg()`?

*Mini-Demo Ideas:*

```python
import pandas as pd
import re

# Basic regex with Pandas
phones = pd.Series(['(123) 456-7890', '555-123-4567', '1234567890'])
# Remove non-digits
clean = phones.str.replace(r'\D', '', regex=True)
print(clean)

# Extract patterns
logs = pd.Series(['[2023-10-26 10:00:00] INFO: Started'])
pattern = r'\[([^\]]+)\] (\w+): (.+)'
extracted = logs.str.extract(pattern)
print(extracted)

# GroupBy with transform
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'Bob'],
    'Zip': ['12345', '67890', '12346', '67890']
})

# Fix anomalies using mode within groups
def fix_zip(group):
    mode_val = group.mode()
    if mode_val.empty:
        return group
    return group.fillna(mode_val.iloc[0])

df['Zip_Fixed'] = df.groupby('Name')['Zip'].transform(fix_zip)
```

## Apply Prompts (Live Coding & Troubleshooting)

### Assignment Hotspots
- Regex syntax is dense and unforgiving
- Understanding `groupby().transform()` pattern
- The `fix_anomaly()` function with `mode()` and voting
- Installing/importing `thefuzz` in Kaggle

### Try This Live

**Let's debug a regex pattern:**

```python
# Extract timestamp, level, and message
pattern = r'\[([^\]]+)\] (\w+): (.+)'
log = "[2023-10-26 10:00:00] INFO: User logged in"

result = pd.Series([log]).str.extract(pattern)
print(result)
```

Ask:
- What does `[^\]]+` mean? (Match anything except `]`)
- What do the parentheses do? (Create capture groups)
- How many columns will this create?

## Common Regex Patterns (for reference)

```python
# Remove non-digits
r'\D'

# Match email domains
r'@([\w\.-]+)'

# Match phone numbers
r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

# Extract date parts
r'(\d{4})-(\d{2})-(\d{2})'

# Match word at start
r'^\w+'
```

## Engagement Strategies (for quiet groups)

- "Let's predict what this regex will match"
- "Can someone explain what `mode()` returns?"
- "What happens if all values in a group are different?"

## Optional Challenges

- Extract email addresses from text using regex
- Implement fuzzy matching with a custom threshold
- Create a multi-step cleaning pipeline

✅ Mentor To-Do
- [ ] Run a session using this guide
- [ ] Help students understand regex patterns (it's okay to look them up!)
- [ ] Submit your [Mentor Session Report](https://airtable.com/appoSRJMlXH9KvE6w/shrp0jjRtoMyTXRzh)
