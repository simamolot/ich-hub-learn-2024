# 1. Напишите программу, которая запрашивает у пользователя строку и определяет,
# является ли она панграммой.
# Панграмма - это фраза, содержащая все буквы алфавита.
# Программа должна игнорировать регистр букв и пробелы при проверке панграммы.
# Выведите соответствующее сообщение на экран с помощью команды print.
# Решить задачу для латиницы.
# Пример вывода:
# Введите строку: The quick brown fox jumps over the lazy dog
# Строка является панграммой.

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sentence = input("Enter a sentence: ").upper()
i = 0

while i < len(alphabet):
    if alphabet[i] not in sentence:
        print("This is not a pangram.")
        break
    i += 1
else:
    print("This is a pangram.")

# 2. Напишите программу, которая запрашивает у пользователя строку и выводит на экран
# количество гласных и согласных букв в ней.
# Используйте функцию len() для подсчета количества букв.
# Выведите результат на экран с помощью команды print.
# Решить задачу для латиницы.
# Пример вывода:
# Введите строку: Hello World
# Количество гласных букв: 3
# Количество согласных букв: 7

vowels = "AEIOUY"
consonants = "BCDFGHJKLMNPQRSTVWXZ"
input_string = input("Enter a string: ").upper()
vowel_count = 0
consonant_count = 0

for char in input_string:
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)


