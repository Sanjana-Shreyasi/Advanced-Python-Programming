#Assignment : 9
import csv
import json

data = [
    {"name": "rahul", "marks": "85"},
    {"name": "priya", "marks": "90"},
    {"name": "aman", "marks": "78"}
]

# writing sample data to csv file first
with open("students.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "marks"])
    writer.writeheader()
    writer.writerows(data)

print("Csv file created")

# reading csv file
result = []

with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        result.append(row)

print("Data read from csv is")
print(result)

# writing data to json file
with open("students.json", "w") as f:
    json.dump(result, f, indent=4)

print("Json file created successfully")

with open("students.json", "r") as f:
    print("Content of json file is")
    print(f.read())

#Output
'''Csv file created
Data read from csv is
[{'name': 'rahul', 'marks': '85'}, {'name': 'priya', 'marks': '90'}, {'name': 'aman', 'marks': '78'}]
Json file created successfully
Content of json file is
[
    {
        "name": "rahul",
        "marks": "85"
    },
    {
        "name": "priya",
        "marks": "90"
    },
    {
        "name": "aman",
        "marks": "78"
    }
]'''