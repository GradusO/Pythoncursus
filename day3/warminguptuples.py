persons = [("Reindert", "Ekker", 25),
           ("Joris", "Hoendervangers", 24),
           ("Jeroen", "Meijer", 23)]

def get_person(index):
    person = persons[index]
    return (person[0], person[1], person[2])

num = int(input("Give a number [0-2]? "))
firstname, lastname, age = get_person(num)
print(f"This person is called {firstname} {lastname} and is {age} years old.")