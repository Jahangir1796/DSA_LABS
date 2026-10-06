# ##########  CLASS WORK PRACTICE  #####################

# # ******LAB 03 SECTION O1 (DataFrames, Series and Reading Real Files)********


# # -----1-------
# import pandas as pd
# df = pd.DataFrame({
#     'name':  ['ali', 'sara', 'omar', 'hina'],
#     'hours': [2, 8, 5, 1],
#     'score': [50, 88, 70, 40],
#     'result': ['fail', 'pass', 'pass', 'fail']
# })
# print(df)
# col = df['score']
# print("\ntype of a column:", type(col).__name__)
# print("mean score:", col.mean())


# # ---------2--------
# import pandas as pd
# df = pd.DataFrame({'name': ['ali','sara'], 'score': [50, 88]})
# # WRONG: writes the index as a column
# df.to_csv('bad.csv')
# print("re-read bad.csv:\n", pd.read_csv('bad.csv'))
# # RIGHT:
# df.to_csv('good.csv', index=False)
# print("re-read good.csv:\n", pd.read_csv('good.csv'))


# # --------3------
# import pandas as pd, numpy as np
# df = pd.DataFrame({
#     'age':   [22, 35, np.nan, 19, 28],
#     'score': [88, 72, 55, 91, np.nan],
#     'batch': ['A','B','A','B','A'],
# })
# print("HEAD:\n", df.head(2))
# print("SHAPE:", df.shape)
# print("INFO:"); df.info()
# print("DESCRIBE:\n", df.describe())
# print("NULLS:\n", df.isnull().sum())


# # ----4-----
# import pandas as pd
# df = pd.DataFrame(
#     {'hours': [2, 8, 5, 1], 'score': [50, 88, 70, 40]},
#     index=['ali', 'sara', 'omar', 'hina'])
# print("loc label 'sara':\n", df.loc['sara'])
# print("iloc position 1 :\n", df.iloc[1])
# print("loc rows+col    :", df.loc[['ali','omar'], 'score'].tolist())
# print("iloc block      :\n", df.iloc[0:2, 0:2])   # index from 0 to 2 (will print 0 and 1 index values not 2)


# # ------5----
# import pandas as pd
# df = pd.DataFrame({
#     'product': ['A','B','C'], 'price': [100, 250, 80], 'qty': [3, 1, 5]})
# df.to_json('data.json')                     # write JSON
# back = pd.read_json('data.json')            # read it back
# back['revenue'] = back['price'] * back['qty']
# back.to_csv('report.csv', index=False)      # export as CSV
# print(pd.read_csv('report.csv'))



# import pandas as pd 
# df = pd.DataFrame({
#     'price': ['100', '250', 'N/A', '120'],
# })

# print(df['price'].sum())

# df['price'] = pd.to_numeric(df['price'], errors='coerce')  # convert to numeric, coerce errors to NaN
# print(df['price'].mean().round(2))  # calculate mean of the 'price' column


# *****************TASKS ANSWER**********

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