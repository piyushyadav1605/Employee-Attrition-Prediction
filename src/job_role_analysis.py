import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("data/raw/employee_attrition.csv")
job_role_count=df["JobRole"].value_counts()
print("="*70)
print("Job Role Distribution")
print("="*70)
for job_role, count in job_role_count.items():
    print(f"{job_role:<25} : {count}")
left_employees=df[df["Attrition"]=="Yes"]
left_job_role_count=left_employees.groupby("JobRole").size()    
job_role_attrition_rate=left_job_role_count/job_role_count*100
print("="*70)
print("Attrition Rate by Job Role")
print("="*70)   
job_role_attrition_rate.sort_values(ascending=False, inplace=True)
print("Attrition Rate by Job Role ")
print(job_role_attrition_rate)
print("="*70)
print("Top 5 Job Roles with Highest Attrition Rate")
print("="*70)
top_5_roles = job_role_attrition_rate.head(5)
print(top_5_roles)
top_5_left_count = left_job_role_count[top_5_roles.index]
print("="*70)
print("Top 5 Job Roles with Highest Attrition Count")
print("="*70)
for job_role, count in top_5_left_count.items():
    print(f"{job_role:<25} : {count}")
plt.figure(figsize=(9,5))
bars=plt.bar(top_5_roles.index, top_5_roles.values)
plt.title("Top 5 Job Roles with Highest Attrition Rate")
plt.xlabel("Job Role")
plt.ylabel("Attrition Rate (%)")
for bar in bars:
    height=bar.get_height()
    x=bar.get_x()+bar.get_width()/2
    y=height+1
    plt.text(x, y, f"{height:.2f}%")
plt.xticks(rotation=45)
plt.ylim(0, max(top_5_roles.values)+10)
plt.tight_layout()
plt.savefig("images/top_5_job_roles_with_highest_attrition_rate.png", )   
plt.show() 

