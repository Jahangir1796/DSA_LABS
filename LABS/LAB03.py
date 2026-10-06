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