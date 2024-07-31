#  Напишите программу, которая запрашивает у пользователя два логических значения
#  (True или False) и выводит результаты следующих логических операций:
#
# - Логическое И (and) между двумя значениями.- Логическое ИЛИ (or) между двумя значениями.
#  - Логическое НЕ (not) для каждого значения.
# - Результат сравнения двух значений на равенство.
# - Результат сравнения двух значений на неравенство.
# Результаты должны быть выведены с помощью команды print.
# Пример вывода:
# Введите первое логическое значение (True или False): True
# Введите второе логическое значение (True или False): False
# Результат логического И: False
# Результат логического ИЛИ: True
# Результат логического НЕ (для первого значения): False
# Результат логического НЕ (для второго значения): True
# Результат сравнения на равенство: False
# Результат сравнения на неравенство: True


a = input("Enter value for a (True or False): ")
b = input("Enter value for b (True or False): ")

if a == "True":
    a = True
if a == "False":
    a = False
if b == "True":
    b = True
if b == "False":
    b = False

print("Result and:", a and b)
print("Result  or:", a or b)
print("not (for the first value):", not a)
print("not (for the second value):", not b)
print("equality comparison:", a == b)
print("inequality comparison:", a != b)
