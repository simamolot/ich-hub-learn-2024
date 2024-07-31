# 1. Напишите функцию merge_dicts, которая принимает произвольное количество словарей в качестве аргументов
# и возвращает новый словарь, объединяющий все входные словари. Если ключи повторяются, значения должны быть объединены
# в список. Функция должна использовать аргумент **kwargs для принятия произвольного числа аргументов словаря.
# Пример ввода:
# {'a': 1, 'b': 2}
# {'b': 3, 'c': 4}
# {'c': 5, 'd': 6}
#
# Пример вывода:
# {'a': [1], 'b': [2, 3], 'c': [4, 5], 'd': [6]}

def merge_dicts(**kwargs):
    result = {}
    for dictionary in kwargs.values():
        for key, value in dictionary.items():
            if key in result:
                if isinstance(result[key], list):
                    result[key].append(value)
                else:
                    result[key] = [result[key], value]
            else:
                result[key] = [value]
    return result


result = merge_dicts(
    dict1={'a': 1, 'b': 2},
    dict2={'b': 3, 'c': 4},
    dict3={'c': 5, 'd': 6}
)
print(result)


# 2. Напишите программу, которая принимает строку от пользователя и подсчитывает количество
# уникальных символов в этой строке. Создайте функцию count_unique_chars, которая принимает строку и
# возвращает количество уникальных символов. Выведите результат на экран.
#
# Пример вывода:
# Введите строку: hello
# Количество уникальных символов: 4

def count_unique_chars(string):
    return len(set(string))


input_string = input("Введите строку: ")
result = count_unique_chars(input_string)
print(f"Количество уникальных символов: {result}")


# 3. Напишите программу, которая создает словарь, содержащий информацию о студентах и их оценках.
# Ключами словаря являются имена студентов, а значениями - списки оценок. Создайте функцию calculate_average_grade,
# которая принимает словарь с оценками студентов и вычисляет средний балл для каждого студента. Функция должна возвращать
# новый словарь, в котором ключами являются имена студентов, а значениями - их средний балл. Выведите результат на экран.
#
# Пример словаря с оценками
# grades = {
#
#     'Alice': [85, 90, 92],
#
#     'Bob': [78, 80, 84],
#
#     'Carol': [92, 88, 95]
#
# }
# Пример вывода:
# {'Alice': 89.0, 'Bob': 80.66666666666667, 'Carol': 91.66666666666667}

def calculate_average_grade(grades):
    return {student: sum(scores) / len(scores) for student, scores in grades.items()}



grades = {
    'Alice': [85, 90, 92],
    'Bob': [78, 80, 84],
    'Carol': [92, 88, 95]
}

result = calculate_average_grade(grades)
print(result)
