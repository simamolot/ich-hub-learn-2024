# 1. Напишите программу, которая принимает список чисел от пользователя и передает его в функцию modify_list,
# которая изменяет элементы списка. Функция должна умножить нечетные числа на 2, а четные числа разделить на 2.
# Выведите измененный список на экран. Объясните, почему изменения происходят только внутри функции и как работают
# изменяемые и неизменяемые параметры.
# Пример вывода:
# Введите список чисел, разделенных пробелами: 1 2 3 4 5
# Измененный список чисел: [2, 1, 6, 2, 10]

mass = list(map(int, input('Введите список чисел, разделенных пробелами:').split()))


def modify_list():
    for index in range(len(mass)):
        if mass[index] % 2 != 0:
            mass[index] *= 2
        else:
            mass[index] /= 2


modify_list()
print(mass)


# 2. Напишите программу, которая принимает произвольное количество аргументов от пользователя и передает их в функцию
# calculate_sum, которая возвращает сумму всех аргументов. Используйте оператор * при передаче аргументов в функцию.
# Выведите результат на экран.
#
# Пример вывода:
# Введите числа, разделенные пробелами: 1 2 3 4 5
# Сумма чисел: 15


numbers = map(int, input("Введите числа, разделенные пробелами: ").split())
def calculate_sum(*args):
    return sum(args)



print(f"Сумма чисел: {calculate_sum(*numbers)}")