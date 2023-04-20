grades = {
'John': [8, 2, 3, 6, 8],
'Annie': [5, 8, 7, 8, 5],
'Pete': [8, 8, 6, 7, 9],
'Lucy': [2, 4, 5, 6, 7],
'Bob': [6, 7, 5, 6, 7]
}

name = input("What is the student name?")
if name in grades:
    print(name, ":\n")
    print(grades[name])
else:
    print("The student is not in the list")