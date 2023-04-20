income = int(input("Your income ? "))
if income < 20000:
    print("You don't have to pay taxes!")
if income > 20000 and income < 50000:
    print("You have to pay 30%")
else:
    print("You have to pay 60%")