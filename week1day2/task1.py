
import csv
import json

names = ["Arun", "Priya", "Rahul", "Divya", "Karthik"]

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

print("Names written successfully!")


with open("names.txt", "r") as file:
    for i, name in enumerate(file, start=1):
        print(f"{i}. {name.strip()}")


students = [
    {"name": "Arun", "marks": 55},
    {"name": "Priya", "marks": 60},
    {"name": "Rahul", "marks": 72},
    {"name": "Divya", "marks": 88},
    {"name": "Karthik", "marks": 45}
]

with open("students.csv", "w", newline="") as file:
    fieldnames = ["name", "marks"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)


print("\nStudents scoring above 60:")

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for student in reader:
        if int(student["marks"]) > 60:
            print(f"Above 60: {student['name']} {student['marks']}")



with open("students.json", "w") as file:
    json.dump(students, file, indent=2)

print("\nJSON file created successfully!")


with open("students.json", "r") as file:
    data = json.load(file)

print("\nStudents from JSON:")

for student in data:
    print(student["name"], "-", student["marks"])


try:
    with open("missing.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("\nmissing.txt -> File not found")
