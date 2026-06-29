import json

with open("students.json", encoding="utf-8") as file:
    data = json.load(file)

# for student in data:
#     print(student.get("name"))

# print("\n\nPythonda o'qiyotganlar:")
# for student in data:
#     courses = student.get("courses")
#     if "Python" in courses:
        # print(student.get("name"))
        
course_names = set()
for student in data:
    courses = student.get("courses")
    course_names.update(courses)

counter = {}
for c in course_names:
    for student in data:
        courses = student.get("courses")
        if c in courses:
            counter.setdefault(c, 0)
            counter[c] += 1

for name, count in sorted(counter.items()):
    print(f"{name} - {count}")