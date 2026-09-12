import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/employee_attrition.csv")

monthly_income_stats = df["MonthlyIncome"]
print("=" * 70)
print("Monthly Income Statistics")
print("=" * 70)

print(monthly_income_stats.min())

print(monthly_income_stats.max())

print(monthly_income_stats.mean())

print(monthly_income_stats.median())

df["IncomeGroup"] = pd.cut(

    df["MonthlyIncome"],

    bins=[0, 3000, 6000, 10000, 20000],

    labels=["Low", "Medium", "High", "Very High"]

)

income_group_count = df["IncomeGroup"].value_counts()
print("=" * 70)
print("Income Group Distribution")
print("=" * 70)

print(income_group_count)

left_employees = df[df["Attrition"] == "Yes"]

left_income_count = left_employees.groupby(left_employees["IncomeGroup"]).size()
print("=" * 70)
print("Left Employees by Income Group")
print("=" * 70)

print(left_income_count)

income_attrition_rate = (left_income_count / income_group_count) * 100
print("=" * 70)
print("Attrition Rate by Income Group")
print("=" * 70)

print(income_attrition_rate)

income_attrition_rate.sort_values(ascending=False, inplace=True)
print("=" * 70)
print("Attrition Rate by Income Group (Sorted)")    
print("=" * 70)

print(income_attrition_rate)

plt.figure(figsize=(8,5))

bars = plt.bar(income_attrition_rate.index, income_attrition_rate.values)

plt.title("Attrition Rate by Income Group")

plt.xlabel("Income Group")

plt.ylabel("Attrition Rate (%)")

plt.ylim(0, max(income_attrition_rate.values) + 10)

for bar in bars:

    height = bar.get_height()

    x = bar.get_x() + bar.get_width() / 2

    y = height + 1

    plt.text(x, y, f"{height:.2f}%")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("images/attrition_rate_by_income_group.png")

plt.show()