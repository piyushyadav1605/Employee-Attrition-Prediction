import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/employee_attrition.csv")

satisfaction_count=df["JobSatisfaction"].value_counts().sort_index()
left_employees = df[df["Attrition"] == "Yes"]

left_satisfaction_count = left_employees.groupby("JobSatisfaction").size()
satisfaction_attrition_rate = (left_satisfaction_count / satisfaction_count)*100

print(left_satisfaction_count)
print(satisfaction_count)
print(satisfaction_attrition_rate)
plt.figure(figsize=(8,5))

bars = plt.bar(
    satisfaction_attrition_rate.index,
    satisfaction_attrition_rate.values
)
plt.xlabel("Job Satisfaction")
plt.ylabel("Attrition Rate")
for bar in bars:
    height = bar.get_height()
    x = bar.get_x() + bar.get_width() / 2
    plt.text(x, height + 0.01, f"{height:.2f}", ha='center', va='bottom')
plt.title("Attrition Rate by Job Satisfaction")
plt.xticks(rotation=45)
plt.ylim(0, max(satisfaction_attrition_rate.values) + 0.1)
plt.tight_layout()
plt.show()