# 1. Напишите генератор, который будет принимать на вход числа и возвращать их сумму. Генератор должен использовать
# инструкцию yield для возврата текущей суммы и должен продолжать принимать новые числа для добавления к сумме. Если
# генератор получает на вход число 0, он должен прекращать работу и вернуть окончательную сумму. Напишите программу,
# которая будет использовать этот генератор для пошагового расчета суммы чисел, вводимых пользователем.
#
# Пример вывода:
# Введите числа для суммирования (0 для окончания):
#
# Введите число: 3
#
# Текущая сумма: 3
#
# Введите число: 5
#
# Текущая сумма: 8
#
# Введите число: 2
#
# Текущая сумма: 10
#
# Введите число: 0
#
# Текущая сумма: 10

def sum_generator():
    total = 0
    while True:
        number = yield total
        if number == 0:
            break
        total += number


print("Enter numbers (0 to finish):")
gen = sum_generator()
next(gen)

while True:
    try:
        number = int(input("Number: "))
        current_sum = gen.send(number)
        print(f"Current sum: {current_sum}")
        if number == 0:
            break
    except ValueError:
        print("Please enter a valid number.")


# 2. Напишите генератор, который будет генерировать арифметическую прогрессию
def arithmetic_progression(start, step, count):
    current = start
    for _ in range(count):
        yield current
        current += step


for number in arithmetic_progression(1, 2, 10):
    print(number)
