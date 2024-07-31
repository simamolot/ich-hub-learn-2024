# 1. Напишите программу, которая запрашивает у пользователя его имя, возраст и место проживания,
# а затем выводит их в следующем формате:
# "Привет, меня зовут {0}. Мне {1} лет. Я живу в {2}."
# Вместо {0}, {1} и {2} подставьте соответствующие значения. Используйте метод format() для форматирования строки.
# Потом попробуйте использовать f-строку. Выведите результат на экран с помощью команды print.
#

name = input('Enter your name: ')
age = int(input('Enter your age: '))
city = input('Enter where you live: ')

print("Hello my name is {0}. I'am {1} years old. I'am living in {2}.".format (name, age, city))

print(f"Hello my name is {name}. I'am {age} years old. I'am living in {city}.")

# Напишите программу, которая запрашивает у пользователя два числа и выводит их сумму и произведение в следующем формате:
# "Сумма: {sum:.2f}, Произведение: {product:.2f}"
# Вместо {sum:.2f} и {product:.2f} подставьте соответствующие значения, округленные до двух десятичных знаков.
# Используйте f-строки с использованием форматных спецификаторов для форматирования чисел. Выведите результат на
# экран с помощью команды print.

number_1 = float(input('Enter the first number: '))
number_2 = float(input('Enter the second number: '))

sum = number_1 + number_2
product = number_1 * number_2

print(f"Summery: {sum:.2f}, Output: {product:.2f}")



