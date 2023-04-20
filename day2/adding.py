# l = [10, 20, 30, 40, 50]
# print(l[1])
# print(l[-2])

# l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# number = int(input("Geef een getal? "))
# index = int(input("Geef en index "))
#
# l[index] += number
# print(l)

l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
number = int(input("Geef een getal? "))
index = int(input("Geef en index? "))

l.insert(index, number)
print(l)