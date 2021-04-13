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
clean_df['Mid-Career Median Salary'].max()

# College major that has the lowest starting salary
clean_df['Undergraduate Major'][clean_df['Starting Median Salary'].idxmin()]
# How much?
clean_df['Starting Median Salary'][clean_df['Starting Median Salary'].idxmin()]

# Lowest mid career salary
clean_df['Undergraduate Major'][clean_df['Mid-Career Median Salary'].idxmin()]
clean_df['Mid-Career Median Salary'][clean_df['Mid-Career Median Salary'].idxmin()]

# Low risk spread
# Insert Spread column
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
# Sort
low_risk = clean_df.sort_values('Spread')
print("Low Risk")
print(low_risk[['Undergraduate Major', 'Spread']].head())

# Highest values in 90th percentile
print("Highest Potential")
clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False).head()

# Greatest spread in salaries
print("Greatest spread in salaries")
highest_spread = clean_df.sort_values('Spread', ascending=False)
highest_spread[['Undergraduate Major', 'Spread']].head()

# Group by function to make table of entries per group
clean_df.groupby('Group').count()
# Group by function to get average
clean_df.groupby('Group').mean()
