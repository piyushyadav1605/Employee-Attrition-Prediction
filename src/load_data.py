import pandas as pd

df = pd.read_csv("data/raw/employee_attrition.csv")


print("=" * 70)
print("Shape")
print(df.shape)

print("=" * 70)
print("Columns")
print(df.columns.tolist())

print("=" * 70)
print("Missing Values")
print(df.isnull().sum())

print("=" * 70)
print("Duplicate Rows")
print(df.duplicated().sum())

print("=" * 70)
print("Statistical Summary")
print(df.describe())