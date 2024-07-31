#Task 1

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))


if a <= b <= c:
    print("{a}, {b}, {c}")
elif a <= c <= b:
    print("{a}, {c}, {b}")
elif b <= a <= c:
    print("{b}, {a}, {c}")
elif b <= c <= a:
    print("{b}, {c}, {a}")
elif c <= a <= b:
    print("{c}, {a}, {b}")
else:
    print(" {c}, {b}, {a}")

#Task 2
year = int(input("Enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
     print("The year is a leap year.")
else:
     print("The year is not a leap year.")
