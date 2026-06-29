import json

with open("students.json", encoding="utf-8") as file:
    data = json.load(file)

for student in data:
    print(student.get("name"))

print("\n\nPythonda o'qiyotganlar:")
for student in data:
    courses = student.get("courses")
    if "Python" in courses:
        print(student.get("name"))
