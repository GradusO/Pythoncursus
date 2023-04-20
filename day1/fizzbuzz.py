count = 1
while count <= 100:
    if count % 3 == 0:
        if count % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif count % 5 == 0:
        print("Buzz")
    else:
        print(count)
    count += 1