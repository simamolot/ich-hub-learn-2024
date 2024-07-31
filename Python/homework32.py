# 1. Реализовать класс Counter, который представляет счетчик. Класс должен поддерживать следующие операции:
# - Увеличение значения счетчика на заданное число (оператор +=)
# - Уменьшение значения счетчика на заданное число (оператор -=)
# - Преобразование счетчика в строку (метод __str__)
# - Получение текущего значения счетчика (метод __int__)
# Пример использования:
# counter = Counter(5)
# counter += 3
# print(counter)  # Вывод: 8
# counter -= 2
# print(int(counter))  # Вывод: 6

class Counter:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        return Counter(self.value + other)

    def __sub__(self, other):
        return Counter(self.value - other)

    def __str__(self):
        result = f'{self.value}'
        return result


counter = Counter(5)
counter += 3
print(counter)  # Вывод: 8
counter -= 2
print(counter)  # Вывод: 6
