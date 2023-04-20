# sum = 0
# count = 0
# while True:
#     grade = int(input("Enter a grade?"))
#     if grade == -1:
#         break
#         # issue when sum is exactly below break
#     sum += grade
#     count += 1
#
# print("Average", sum/count)


sum = 0
count = 0
max = 0
while True:
    grade = int(input("Enter a grade? "))
    if grade == -1:
        break
    if grade > max:
        max = grade
    sum += grade
    count += 1

print("Average: ", sum/count)
print("Highest: ", max)

