l = []
for i in range(4):
    l.append(input("A word? "))

print(sorted(l))
print(sorted(l, reverse=True))

for a in l:
    print(a.upper())
    print(a[0])
