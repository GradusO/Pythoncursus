with open("words_with_a.txt") as f:
    count = 0
    for l in f:
        if len(l) == 5:
            count += 1
print(count)

# f = open("words_with_a.txt")
# count = 0
# for line in f:
#     # Line length includes newline character
#     if len(line) == 5:
#         count += 1
# print(count)