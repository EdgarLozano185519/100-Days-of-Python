import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")
df.head()
df.shape
df.isna()
clean_df = df.dropna()
clean_df.tail()
clean_df['Starting Median Salary'].idxmax()
clean_df['Undergraduate Major'][43]

# Highest mid career salary major
salary_id = clean_df['Mid-Career Median Salary'].idxmax()
clean_df['Undergraduate Major'][salary_id]
df_clean['Mid-Career Median Salary'].max()
