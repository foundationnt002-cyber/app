import json

with open("students.json", encoding="utf-8") as file:
    data = json.load(file)

for student in data:
    print(student.get("name"))