l = []
while True:
    word = input("A word please? ")
    if word in l:

    if not word:
        break
    l.append(word)
print(l)