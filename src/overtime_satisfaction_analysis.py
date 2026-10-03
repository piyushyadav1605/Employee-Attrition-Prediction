import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/employee_attrition.csv")
combination_count = df.groupby(
    ["OverTime", "JobSatisfaction"]
).size()
print("=" * 70)
print("Employee count by Overtime and Job Satisfaction")
print("=" * 70)
print(combination_count)
left_employees = df[df["Attrition"] == "Yes"]
left_combination_count = left_employees.groupby(
    ["OverTime", "JobSatisfaction"]).size()

print("=" * 70)
print("Left Employees by Overtime and Job Satisfaction")
print("=" * 70)
print(left_combination_count)
combined_attrition_rate = (left_combination_count / combination_count) * 100
print("=" * 70)
print("Combined Attrition Rate")
print("=" * 70)
print(combined_attrition_rate)
rate_table = combined_attrition_rate.unstack()
print("=" * 70)
print("Attrition Rate Table")
print("=" * 70)
print(rate_table)

ax = rate_table.plot(kind="bar", figsize=(10, 6))

for container in ax.containers:
    ax.bar_label(
        container,
        fmt="%.2f%%",
        padding=3
    )

plt.title("Attrition Rate by Overtime and Job Satisfaction")
plt.xlabel("Overtime")
plt.ylabel("Attrition Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("images/attrition_rate_by_overtime_and_job_satisfaction.png")
plt.show()

