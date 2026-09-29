import pandas as pd

# Load the PSV file
df = pd.read_csv("info/raw/p000001.psv", sep="|")

# Display the first 10 rows
print(df.head(10).to_string())

# Display the column names
print("\nColumns:")
print(df.columns.tolist())

# Display the size of the data
print("\nShape:")
print(df.shape)