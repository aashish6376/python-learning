student = {
    "name": "Aashish",
    "age": 22,
    "city": "Jaipur"
}
for key in student:
    print(key, ":", student[key])
for key in student:
    print(key)
for value in student.values():
    print(value)
for key, value in student.items():
    print(key , ":" , value)
for key, value in student.items():
    print(value)
marks = {
    "Maths" : 90,
    "English" : 89,
    "Science" : 97
}
for x, y in marks.items():
    print(x, ":", y)