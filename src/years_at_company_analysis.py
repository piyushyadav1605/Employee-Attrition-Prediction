import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/raw/employee_attrition.csv")
print("=" * 70)
print("Years at Company Statistics")
print("=" * 70)
print("Minimum Years:", df["YearsAtCompany"].min())
print("Maximum Years:", df["YearsAtCompany"].max())
print("=" * 70)
print("Years at Company Distribution")
print("=" * 70)
years_count = df["YearsAtCompany"].value_counts().sort_index()

print(years_count)
df["YearsGroup"] = pd.cut(
    df["YearsAtCompany"],
    bins=[-1, 2, 5, 10, 20, 40],
    labels=["0-2", "3-5", "6-10", "11-20", "21+"]  )
years_group_count = df["YearsGroup"].value_counts().sort_index()
print("=" * 70)
print("Years at Company Group Distribution")    
print("=" * 70)
print(years_group_count)
left_employees = df[df["Attrition"] == "Yes"]

left_years_count = left_employees.groupby("YearsGroup").size()
print("=" * 70)
print("Left Employees by Years at Company Group")  
print("=" * 70)
print(left_years_count)
years_attrition_rate = (left_years_count / years_group_count) * 100
print("=" * 70)
print("Attrition Rate by Years at Company Group")
print("=" * 70)
print(years_attrition_rate)
years_attrition_rate.sort_values(ascending=False, inplace=True)
print("=" * 70)
print("Attrition Rate by Years at Company Group (Sorted)")
print("=" * 70)
print(years_attrition_rate)
plt.figure(figsize=(8,5))

bars = plt.bar(
    years_attrition_rate.index,
    years_attrition_rate.values
)

plt.title("Attrition Rate by Years at Company")
plt.xlabel("Years at Company")
plt.ylabel("Attrition Rate (%)")
for bar in bars:
    height = bar.get_height()
    x = bar.get_x() + bar.get_width() / 2
    y = height + 1
    plt.text(x, y, f"{height:.2f}%")
plt.ylim(0, max(years_attrition_rate.values) + 10)
plt.savefig("images/attrition_rate_by_years_at_company.png")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()    