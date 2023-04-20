l =  [
     ['John', 'Smith', 32],
     ['Peter', 'Jones', 50],
     ['Anna', 'Karenina', 44],
     ['Guido', 'Van Rossum', 54]
 ]

gemleeftijd = 0
for i in l:
    print(i[0], i[1])
    gemleeftijd += i[2]

print(gemleeftijd/4)