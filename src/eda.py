import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/employee_attrition.csv")

# Count employees who stayed and left
print("=" * 70)
print("Employee Attrition Summary")
print("=" * 70)
attrition_count = df["Attrition"].value_counts()
left_count = attrition_count["Yes"]
stayed_count = attrition_count["No"]
print(f"Employees Left   : {left_count}")
print(f"Employees Stayed : {stayed_count}")
attrition_percentage = df["Attrition"].value_counts(normalize=True) * 100
left_percentage = attrition_percentage["Yes"]
stayed_percentage = attrition_percentage["No"]
print(f"Attrition Rate : {left_percentage:.2f}%")
print(f"Retention Rate : {stayed_percentage:.2f}%")
print("=" * 70)
