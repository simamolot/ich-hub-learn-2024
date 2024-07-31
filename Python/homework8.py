# 1. Напишите программу, которая запрашивает у пользователя целое число и определяет,
# является ли оно палиндромом. Число является палиндромом, если оно читается
# одинаково слева направо и справа налево. Выведите соответствующее сообщение на
# экран с помощью команды print. Используйте математические операции. Работу со
# строками использовать нельзя.
# Пример вывода:
# Введите целое число: 12321
# Число является палиндромом.

number = int(input("Введите целое число: "))
original_number = number
reverse_number = 0

while number > 0:
    reverse_number = reverse_number * 10 + number % 10
    number //= 10

if original_number == reverse_number:
    print("Число является палиндромом")
else:
    print("Число не является палиндромом")


# 2. Напишите программу, которая запрашивает у пользователя целое число и проверяет,
# является ли оно числом Армстронга. Число Армстронга - это число, которое равно сумме
# своих цифр, возведенных в степень, равную количеству цифр в числе.
# Выведите соответствующее сообщение на экран с помощью команды print.
# Пример вывода:
# Введите целое число: 153
# Число является числом Армстронга.

number = int(input("Enter the integer:  "))
save_number = number
digits = 0

while number > 0:
    number //= 10
    digits += 1

number = save_number
armstrong = 0

while number > 0:
    armstrong += (number % 10) ** digits
    number //= 10

if save_number == armstrong:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")
