# Написать программу, вычисляющую факториал числа.
#
# Решить задачу с помощью рекурсии.

# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# num = 5
# result = factorial(num)
# print(f'Enter the factorial number: {num} = {result}')


# Напишите программу, которая использует рекурсию для вычисления суммы цифр числа.
# Создайте функцию sum_digits, которая принимает один аргумент - число, для которого нужно вычислить сумму цифр.
# Используйте условие выхода из рекурсии, когда число состоит из одной цифры. Выведите результат на экран.
#
# Пример вывода:
# Введите число: 12345
# Сумма цифр числа 12345 равна 15

def sum_digits(num):
    if num < 10:
        return num
    else:
        return num % 10 + sum_digits(num // 10)


number = int(input('Enter the number: '))

print(f'The sum of the digits of {number} is {sum_digits(number)}')

