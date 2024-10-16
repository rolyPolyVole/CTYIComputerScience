counts = int(input("Enter the number of counts: "))

i = 0
while i < counts:
    i += 1

    fizz = i % 3 == 0
    buzz = i % 5 == 0

    if fizz and buzz:
        print("FizzBuzz")
    elif fizz:
        print("Fizz")
    elif buzz:
        print("Buzz")
    else:
        print(i)
