import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/raw/employee_attrition.csv")
overtime_count=df["OverTime"].value_counts()
print("=" * 70)
print("Overtime Summary")
print("=" * 70)
print(f"Employees with Overtime   : {overtime_count['Yes']}")
print(f"Employees without Overtime : {overtime_count['No']}")
left_overtime = df[(df["OverTime"] == "Yes") & (df["Attrition"] == "Yes")]
left_no_overtime = df[(df["Attrition"] == "Yes") & (df["OverTime"] == "No")]

overtime_attrition_rate = (len(left_overtime) / overtime_count["Yes"]) * 100
no_overtime_attrition_rate = (len(left_no_overtime) / overtime_count["No"]) * 100
print("=" * 70)
print("Attrition Rate by Overtime")
print("=" * 70)

print(f"{'Overtime':<20} : {overtime_attrition_rate:.2f}%")
print(f"{'No Overtime':<20} : {no_overtime_attrition_rate:.2f}%")
print("=" * 70)
plt.figure(figsize=(7,5))
overtime=["Overtime", "No Overtime"]
rate=[overtime_attrition_rate, no_overtime_attrition_rate]
bars = plt.bar(overtime, rate)
plt.title("Attrition Rate by Overtime")
plt.xlabel("Overtime Status")
plt.ylabel("Attrition Rate (%)")
for bar in bars:
    height=bar.get_height()
    x=bar.get_x() + bar.get_width() / 2
    y=height + 1
    plt.text(x, y, f"{height:.2f}%")
plt.xticks(rotation=0)
plt.xticks(rotation=0)

plt.ylim(0, max(rate) + 10)



plt.savefig("images/overtime_attrition_rate.png")

plt.show()    