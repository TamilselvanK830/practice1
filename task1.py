
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")


avg_salary = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))

bars = plt.bar(avg_salary.index, avg_salary.values)

plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.bar_label(bars, fmt="%.2f")

plt.tight_layout()
plt.savefig("department_salary.png")
plt.close()

plt.figure(figsize=(8, 5))

plt.hist(df["salary"], bins=5, edgecolor="black")

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("salary_histogram.png")
plt.close()


plt.figure(figsize=(8, 5))

for department, group in df.groupby("department"):
    plt.scatter(
        group["id"],
        group["salary"],
        label=department
    )

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend(title="Department")

plt.tight_layout()
plt.savefig("employee_scatter.png")
plt.close()



months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [1200, 1500, 1400, 1800, 2200, 2500]

plt.figure(figsize=(8, 5))

plt.plot(months, sales, marker="o")

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)

plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.close()

print("All 4 charts created and saved successfully!")
