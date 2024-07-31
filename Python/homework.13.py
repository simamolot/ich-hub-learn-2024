# 1. Напишите программу, которая принимает два числа и возвращает их сумму и произведение в виде кортежа (sum, product).
# Используйте функцию для вычисления суммы и произведения.
# Выведите результат на экран с помощью команды print.

def sum_1(a, b):
    return a + b, a * b


a = int(input("Enter a number to add: "))
b = int(input("Enter a number to multiply: "))
c = sum_1(a, b)
print(f'Sum and product: {c}')

# Напишите программу, которая принимает список чисел и возвращает сумму, минимальное и максимальное значение из
# (списк Используйте) функцию для обработки списка чисел и возврата трех значений. Выведите результат на экран с
# помощью команды print.
#
# Пример вывода:
# Введите числа:  3, 7, 2, 9, 1, 5
# Сумма чисел: 27
# Минимальное значение: 1
# Максимальное значение: 9

def numbers(a):
    sum_1 = sum(a)
    sum_2 = min(a)
    sum_3 = max(a)
    return sum_1, sum_2, sum_3


a = list(map(int, input('Enter the number with comma: ').split(', ')))

b = numbers(a)
print(f'The sum number is: {sum(a)}')
print(f'The minimal number is: {min(a)}')
print(f'The maximal number is: {max(a)}')


