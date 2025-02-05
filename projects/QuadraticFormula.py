import math

a = float(input("Enter a\n>>> "))
b = float(input("Enter b\n>>> "))
c = float(input("Enter c\n>>> "))

if a == 0:
    print("Get out")
    exit(1)

minus_b = -b
two_a = 2 * a
discriminant = (b ** 2) - 4 * a * c

if discriminant < 0:
    print("No real solutions")
    exit(1)

solution_1 = (minus_b + math.sqrt(discriminant)) / two_a
solution_2 = (minus_b - math.sqrt(discriminant)) / two_a

print(solution_1)
print(solution_2)
