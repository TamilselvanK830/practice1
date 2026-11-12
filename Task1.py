
Name = input("Enter the Name:")  #str
Age = int(input("Enter the Age:"))  #int
Salary = float(input("Enter the Salary:"))  #float
Order_id = input("Enter items order_id: ").split(",")   #list
Employee = { "Name": Name,"department": "AI/ML ENGINEER"}    #Dict
Numbers = set(input("Enter random numbers: ").split(","))   #set
Values = tuple(input("Enter values: ").split(","))    #Tuple

"""
print("Name: ", Name," ",type(Name))
print("Age: ", Age," ",type(Age))
print("Salary: ", Salary," ",type(Salary))
print("Order_id: ", Order_id," ",type(Order_id))
print("Employee: ", Employee," ",type(Employee))
print("Numbers: ", Numbers," ",type(Numbers))
print("Values: ", Values," ",type(Values))
"""

print("------------Details_And_Data_Types-----------")
Data = {
    "Name": Name,
    "Age": Age,
    "Salary": Salary,
    "Order_id": Order_id,
    "Employee": Employee,
    "Numbers": Numbers,
    "Values": Values
}

for i, value in Data.items():
    print(i, ":", value, "  ", type(value))    #for loop


sales = [12000, 0, 8500, 15000, -200, 9800]
total = 0

print("------------Sales_Report-----------")
for sale in sales:
    if sale <= 0:
        print("Skipped invalid value:", sale)
        continue

    total += sale

    print("Added:", sale, "| Total:", total)

    if total > 30000:
        break

print("------------Final_Report-----------")

if total > 30000:
    print("Target reached. Stopped at:", total)

elif total == 30000:
    print("Target exactly reached. Total:", total)

else:
    print("Target not reached. Total:", total)

