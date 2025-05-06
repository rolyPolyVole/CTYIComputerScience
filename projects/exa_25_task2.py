even = 0
odd = 0

i = 0
while i < 10:
    user_input = int(input(f"Enter number #{i + 1}\n>>> "))

    if user_input % 2 == 0:
        even += 1
    else:
        odd += 1

    i += 1

print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")
