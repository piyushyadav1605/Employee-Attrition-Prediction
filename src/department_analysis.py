import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/employee_attrition.csv")

department_count = df["Department"].value_counts()
print("=" * 70)
for department, count in department_count.items():
    print(f"{department:<25} : {count}")
left_employees = df[df["Attrition"] == "Yes"]
left_department_count = left_employees.groupby("Department").size()
print("=" * 70)
print("Departments with Left Employees")
print("=" * 70)
print(left_department_count)

attrition_rate = (left_department_count / department_count) * 100
print("=" * 70)
print("Attrition Rate by Department")
print("=" * 70)
attrition_rate.sort_values(ascending=False, inplace=True)
for department, rate in attrition_rate.items():
    print(f"{department:<25} : {rate:.2f}%")


