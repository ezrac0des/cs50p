students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])

print("---------------------")

for student in students:
    print(student)

print("---------------------")

for i in range(len(students)):
    print(i + 1, students[i])

print("---------------------")

sts = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print(sts["Hermione"])
print(sts["Harry"])
print(sts["Ron"])
print(sts["Draco"])

print("---------------------")

for st in sts:
    print(st, sts[st], sep=" -> ")

print("---------------------")

stus = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for stu in stus:
    print(stu["name"], stu["house"], stu["patronus"], sep=", ")