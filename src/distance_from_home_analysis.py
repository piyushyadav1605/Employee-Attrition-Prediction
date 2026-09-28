import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/employee_attrition.csv")
print("=" * 70)
print("Distance from Home Statistics")  
print("=" * 70)
print("minimum distance from home:", df["DistanceFromHome"].min())
print("maximum distance from home:", df["DistanceFromHome"].max())
employees_count = df["DistanceFromHome"].value_counts().sort_index()
print("=" * 70)
print("Employee count by distance from home:")
print("=" * 70)
print(employees_count)

df["DistanceGroup"] = pd.cut(
    df["DistanceFromHome"],
    bins=[0, 5, 10, 20, 30],
    labels=["1-5", "6-10", "11-20", "21-30"]
)
print("=" * 70)
print("Distance from Home Group Distribution")
print("=" * 70)
print(df["DistanceGroup"].value_counts().sort_index())
print("=" * 70)
left_employees = df[df["Attrition"] == "Yes"]

left_distance_count = left_employees.groupby("DistanceGroup").size()
print("=" * 70)
print("Left Employees by Distance from Home Group")
print("=" * 70)
print(left_distance_count)

distance_group_count = df["DistanceGroup"].value_counts().sort_index()
distance_attrition_rate = (left_distance_count / distance_group_count) * 100
print("=" * 70)
print("Attrition Rate by Distance from Home Group")
print("=" * 70)
print(distance_attrition_rate)
distance_attrition_rate.sort_values(ascending=False, inplace=True)
print("=" * 70)
print("Attrition Rate by Distance from Home Group (Sorted)")
print("=" * 70)
print(distance_attrition_rate)
plt.figure(figsize=(8,5))

bars = plt.bar(
    distance_attrition_rate.index,
    distance_attrition_rate.values
)

plt.title("Attrition Rate by Distance From Home")
plt.xlabel("Distance From Home (miles)")
plt.ylabel("Attrition Rate (%)")
for bar in bars:
    height = bar.get_height()
    x = bar.get_x() + bar.get_width() / 2
    y = height + 1
    plt.text(x, y, f"{height:.2f}%")
plt.ylim(0, max(distance_attrition_rate.values) + 10)
plt.savefig("images/attrition_rate_by_distance_from_home.png")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()    