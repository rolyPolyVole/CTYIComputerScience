i = 0
counts = int(input("Enter the number of counts: "))

while i < counts:
    i += 1

    fizz = i % 3 == 0
    buzz = i % 5 == 0

    if fizz and buzz:
        print("FizzBuzz")
    elif fizz == 0:
        print("Fizz")
    elif buzz == 0:
        print("Buzz")
    else:
        print(i)