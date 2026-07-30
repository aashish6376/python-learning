students = [
    {"name" : "Aashish", "Age": 22},
    {"name" : "Rahul", "Age": 23},
    {"name" : "Lokesh", "Age": 24}
]
for student in students:
    print(student)
for student in students:
    print(student["name"])
for student in students:
    print(student["name"], "-", student["Age"])
print(students[0])
print(students[0]["name"])
print(students[1]["Age"])