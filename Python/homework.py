# Task 1.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

# Task 2.

radius = float(input("Enter the radius of the circle: "))
pi = 3.14159

circumference = 2 * pi * radius
area = pi * radius ** 2

print(circumference)
print(area)

# Task 3.

x1, y1 = map(float, input(" first point (x1, y1): ").split(','))
x2, y2 = map(float, input("second point (x2, y2): ").split(','))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("Distance between the points:", distance)


