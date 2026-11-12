##########  CLASS WORK PRACTICE  #####################

# ******LAB 03 SECTION O1 (DataFrames, Series and Reading Real Files)********


# -----1-------
import pandas as pd
df = pd.DataFrame({
    'name':  ['ali', 'sara', 'omar', 'hina'],
    'hours': [2, 8, 5, 1],
    'score': [50, 88, 70, 40],
    'result': ['fail', 'pass', 'pass', 'fail']
})
print(df)
col = df['score']
print("\ntype of a column:", type(col).__name__)
print("mean score:", col.mean())


# ---------2--------
import pandas as pd
df = pd.DataFrame({'name': ['ali','sara'], 'score': [50, 88]})
# WRONG: writes the index as a column
df.to_csv('bad.csv')
print("re-read bad.csv:\n", pd.read_csv('bad.csv'))
# RIGHT:
df.to_csv('good.csv', index=False)
print("re-read good.csv:\n", pd.read_csv('good.csv'))


# --------3------
import pandas as pd, numpy as np
df = pd.DataFrame({
    'age':   [22, 35, np.nan, 19, 28],
    'score': [88, 72, 55, 91, np.nan],
    'batch': ['A','B','A','B','A'],
})
print("HEAD:\n", df.head(2))
print("SHAPE:", df.shape)
print("INFO:"); df.info()
print("DESCRIBE:\n", df.describe())
print("NULLS:\n", df.isnull().sum())


# ----4-----
import pandas as pd
df = pd.DataFrame(
    {'hours': [2, 8, 5, 1], 'score': [50, 88, 70, 40]},
    index=['ali', 'sara', 'omar', 'hina'])
print("loc label 'sara':\n", df.loc['sara'])
print("iloc position 1 :\n", df.iloc[1])
print("loc rows+col    :", df.loc[['ali','omar'], 'score'].tolist())
print("iloc block      :\n", df.iloc[0:2, 0:2])   # index from 0 to 2 (will print 0 and 1 index values not 2)


# ------5----
import pandas as pd
df = pd.DataFrame({
    'product': ['A','B','C'], 'price': [100, 250, 80], 'qty': [3, 1, 5]})
df.to_json('data.json')                     # write JSON
back = pd.read_json('data.json')            # read it back
back['revenue'] = back['price'] * back['qty']
back.to_csv('report.csv', index=False)      # export as CSV
print(pd.read_csv('report.csv'))



import pandas as pd 
df = pd.DataFrame({
    'price': ['100', '250', 'N/A', '120'],
})

print(df['price'].sum())

df['price'] = pd.to_numeric(df['price'], errors='coerce')  # convert to numeric, coerce errors to NaN
print(df['price'].mean().round(2))  # calculate mean of the 'price' column


# *****************TASKS ANSWER**************

# 1 
import pandas as pd

# Create two Series
numbers = pd.Series([10, 20, 30, 40, 50])
names = pd.Series(['Ali', 'Sara', 'Omar', 'Hina', 'Ahmed'])

# Combine the Series into a DataFrame
df = pd.DataFrame({
    'Name': names,
    'Number': numbers
})

# Display the DataFrame
print(df)


# 2
import pandas as pd

# Create a DataFrame with 3 rows and 2 columns
df = pd.DataFrame({
    'Name': ['Ali', 'Sara', 'Omar'],
    'Score': [85, 92, 78]
})

# Write DataFrame to CSV without the index
df.to_csv('test.csv', index=False)

# Read the CSV file back
new_df = pd.read_csv('test.csv')

# Display the resulting DataFrame
print(new_df)



# 3
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard'],
    'Price': [120000, 2500, 4500]
})

# Export the DataFrame to JSON
df.to_json('data.json')

# Read the JSON file back into a new DataFrame
new_df = pd.read_json('data.json')

# Display the resulting DataFrame
print(new_df)




# 4 
import pandas as pd

# Load the CSV file
df = pd.read_csv('test.csv')

# 1. Head
print("HEAD:")
print(df.head())

# 2. Shape
print("\nSHAPE:")
print(df.shape)

# 3. Info
print("\nINFO:")
df.info()

# 4. Describe
print("\nDESCRIBE:")
print(df.describe())

# 5. Missing values
print("\nNULLS:")
print(df.isnull().sum())


# 5 
import pandas as pd

# Create a DataFrame with 5 rows and 3 columns
df = pd.DataFrame({
    'Name': ['Ali', 'Sara', 'Omar', 'Hina', 'Ahmed'],
    'Age': [21, 22, 20, 23, 21],
    'Score': [85, 92, 78, 88, 95]
}, index=['student1', 'student2', 'student3', 'student4', 'student5'])

# Select a row using loc by label
print("Using loc:")
print(df.loc['student3'])

# Select a row using iloc by integer position
print("\nUsing iloc:")
print(df.iloc[2])




"""
================================================================================
MUET Cyber Learning Portal - Data Science and Analytics Lab III
Topic: Grouping, Aggregation and Combining Data

SHORT THEORY NOTES:
1. Split-Apply-Combine (groupby):
   - Splits rows into groups based on key categories.
   - Applies an aggregation or transformation function (sum, mean, count) to each group.
   - Combines the per-group answers back into a consolidated pandas Series or DataFrame.
   - Directly maps to the SQL 'GROUP BY' clause.

2. Multi-Metric Aggregation (.agg()):
   - Computes multiple statistical summaries in a single chained call:
     df.groupby('cat')['val'].agg(['mean', 'max', 'count'])
   - Avoids running separate operations and manually stitching tables together.

3. Pivoting (pivot_table):
   - Reshapes tall/long records into a 2D cross-tabulation grid.
   - Maps one categorical variable down rows (index) and another across columns.

4. Merging and Join Logic (pd.merge):
   - Inner Join: Retains only matching keys present in BOTH DataFrames. Unmatched keys are dropped silently.
   - Left Join: Retains all rows from the left DataFrame; unmatched right records become NaN.
   - Outer Join: Retains all records from both sides, populating gaps with NaN.
   - Integrity Rule: Always audit row counts before and after merges to catch silent record losses.
================================================================================
"""

import pandas as pd

print("=" * 65)
print("RUNNING LAB III: GROUPING, AGGREGATION AND COMBINING DATA")
print("=" * 65)


# -------------------------------------------------------------
# TASK 1: Basic GroupBy Aggregation
# Theory: df.groupby('cat')['val'].sum() aggregates values per group.
# -------------------------------------------------------------
print("\n[Executing Task 1: Basic GroupBy Aggregation...]")
df1 = pd.DataFrame({
    'category': ['Alpha', 'Beta', 'Gamma', 'Alpha', 'Beta', 'Gamma', 'Alpha'],
    'value': [15, 25, 40, 35, 10, 50, 20]
})

task1_result = df1.groupby('category')['value'].sum()
print("--- TASK 1 OUTPUT ---")
print(task1_result)


# -------------------------------------------------------------
# TASK 2: Multiple Aggregations with .agg()
# Theory: .agg(['mean', 'max', 'count']) computes multi-column stats in one pass.
# -------------------------------------------------------------
print("\n[Executing Task 2: Multiple Aggregations with .agg()...]")
df2 = pd.DataFrame({
    'batch': ['A', 'B', 'A', 'B', 'A', 'B'],
    'score': [88, 72, 90, 60, 55, 95]
})

task2_result = df2.groupby('batch')['score'].agg(['mean', 'max', 'count'])
print("--- TASK 2 OUTPUT ---")
print(task2_result)


# -------------------------------------------------------------
# TASK 3: Creating a Pivot Table
# Theory: pivot_table converts categorical pairs into a readable matrix grid.
# -------------------------------------------------------------
print("\n[Executing Task 3: Creating a Pivot Table...]")
df3 = pd.DataFrame({
    'batch': ['Batch A', 'Batch A', 'Batch B', 'Batch B', 'Batch A', 'Batch B'],
    'subject': ['Math', 'CS', 'Math', 'CS', 'Math', 'CS'],
    'score': [88, 90, 60, 72, 55, 95]
})

task3_grid = df3.pivot_table(index='batch', columns='subject', values='score', aggfunc='mean')
print("--- TASK 3 OUTPUT ---")
print(task3_grid)


# -------------------------------------------------------------
# TASK 4: Comparing Merge Types
# Theory: Inner drops unmatched keys; left preserves all left-hand records.
# -------------------------------------------------------------
print("\n[Executing Task 4: Comparing Merge Types...]")
left_df = pd.DataFrame({
    'key': [101, 102, 103, 104],
    'student': ['Ali', 'Sara', 'Omar', 'Hina']
})

right_df = pd.DataFrame({
    'key': [101, 102, 103],
    'marks': [88, 92, 79]
})

inner_res = pd.merge(left_df, right_df, on='key', how='inner')
left_res = pd.merge(left_df, right_df, on='key', how='left')

print("--- TASK 4 OUTPUT ---")
print(f"Inner merge row count: {len(inner_res)}")
print(inner_res)
print(f"\nLeft merge row count: {len(left_res)}")
print(left_res)

print("\n" + "=" * 65)
print("ALL 5 TASKS EXECUTED SUCCESSFULLY.")
print("=" * 65)

