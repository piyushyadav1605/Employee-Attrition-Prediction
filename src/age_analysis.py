import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("data/raw/employee_attrition.csv")
minimum_age = df["Age"].min()
maximum_age = df["Age"].max()

print(f"The minimum age of employees is: {minimum_age}")
print(f"The maximum age of employees is: {maximum_age}")
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[17,25,35,45,55, 60],
    labels=["18-25", "26-35", "36-45", "46-55", "56-60"]
)
print(df[["Age", "AgeGroup"]].head(10))
print(df["AgeGroup"].value_counts())
left_employees = df[df["Attrition"] == "Yes"]
left_age_count = left_employees.groupby(left_employees["AgeGroup"]).size()
print(left_age_count)
attrition_rate = (left_age_count / df["AgeGroup"].value_counts()) * 100
attrition_rate.sort_values(ascending=False, inplace=True)
print(attrition_rate)
plt.figure(figsize=(8,5))
bars=plt.bar(attrition_rate.index, attrition_rate.values)
plt.title("Attrition Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Attrition Rate (%)")
for bar in bars:
    height=bar.get_height()
    x=bar.get_x() + bar.get_width() / 2
    y=height + 1
    plt.text(x, y, f"{height:.2f}%")
plt.ylim(0, max(attrition_rate.values) + 10)
plt.savefig("images/attrition_rate_by_age_group.png", )

plt.show()