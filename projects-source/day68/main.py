import pandas as pd

df = pd.read_csv(
    "QueryResults.csv",
    header=0,
    names=['DATE', 'TAG', 'POSTS']
)
print("First Few Rows.")
print(df.head())
print("Last few rows.")
df.tail()
print(df.shape)
df.count()
df.groupby("TAG").sum()
df.groupby("TAG").count()
df.DATE = pd.to_datetime(df.DATE)
df.head()