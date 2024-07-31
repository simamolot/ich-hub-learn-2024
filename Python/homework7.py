# 1. Напишите программу, которая запрашивает у пользователя натуральное десятичное число
# и выводит его двоичное представление. Реализуйте алгоритм перевода числа в двоичную
# систему счисления, используя основные концепции представления чисел (подсказка: через
# деление с остатком). Выведите полученное представление числа на экран.
# Пример вывода:
# Введите натуральное десятичное число: 123
# Двоичное представление числа: 1111011

number = int(input("Enter the prime number: "))
res = ""

while number > 0:
    res = str(number % 2) + res
    number //= 2
    print("double expression: ", res)

print("Binary representation:", res)

# 2. Напишите программу, принимающую число с плавающей точкой и округляющую его до
# целого числа в соответствии с правилами школьной математики. Использовать модуль
# math и методы из него нельзя. Учесть, что программа должна корректно работать с
# отрицательными числами.
# Пример вывода:
# Введите вещественное число: -3.14
# Округленное значение: -3

number = float(input("Введите вещественное число: "))

if number > 0:
    rounded_number = int(number + 0.5)
else:
    rounded_number = int(number - 0.5)

print("Округленное значение:", rounded_number)