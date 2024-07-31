# 1. Напишите функцию find_longest_word, которая будет принимать список слов и возвращать самое длинное слово из списка.
# Аннотируйте типы аргументов и возвращаемого значения функции.
#
# Пример вызова функции и ожидаемого вывода:
# words = ["apple", "banana", "cherry", "dragonfruit"]
# result = find_longest_word(words)
# print(result)  # Ожидаемый вывод: "dragonfruit"

words = ["apple", "banana", "cherry", "dragonfruit"]


def find_longest_word(words: list[str]) -> str:
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


print(find_longest_word(words))

# 2. Напишите программу, которая будет считывать данные о продуктах из файла и использовать аннотации типов для
# аргументов и возвращаемых значений функций. Создайте текстовый файл
# "products.txt", в котором каждая строка будет содержать информацию о продукте в формате "название, цена, количество".
# Например:
# Apple, 1.50, 10
# Banana, 0.75, 15
#
# В программе определите функцию calculate_total_price, которая будет принимать список продуктов и возвращать общую
# стоимость. Продумайте, какая аннотация должна быть у аргумента! Считайте данные из файла, разделите строки на
# составляющие и создайте список продуктов. Затем вызовите функцию calculate_total_price с этим списком и выведите
# результат.
#
# Начиная с этого дз мы потихоньку отказываемся от формата ожидаемого ввода-вывода. Потому что в реальных задачах
# обычно этого нет. Нужно самому придумывать даже самые простые тестовые данные, содержимое тестовых файлов и т.п.
# В случае с классами (будут чуть позже) особенно.

from typing import List, Tuple


def read_products(file_path: str) -> List[Tuple[str, float, int]]:
    products = []
    with open(file_path, 'r') as file:
        for line in file:
            name, price, quantity = line.strip().split(',')
            products.append((name, float(price), int(quantity)))
    return products


def calculate_total_price(products: List[Tuple[str, float, int]]) -> float:
    total = 0.0
    for name, price, quantity in products:
        total += price * quantity
    return total


products = read_products("products.txt")
total_price = calculate_total_price(products)
print(f"The total price of the products: {total_price}")

