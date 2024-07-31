# 1. Напишите программу, которая запрашивает у пользователя строку и преобразует ее,
# удаляя все гласные буквы из строки. Используйте метод replace() для замены гласных букв
# на пустую строку. Выведите преобразованную строку на экран с помощью команды print.
# Введите строку: Hello, world!
# Результат: Hll, wrld!

vowels = "AEIOUYaeiouy"
input_string = input("Enter a string: ")
result = input_string

for vowel in vowels:
    result = result.replace(vowel, "")

print("Result:", result)
#
# 2. Напишите программу, которая запрашивает у пользователя строку и определяет, содержит
# ли она только уникальные символы. Если все символы в строке уникальны, выведите
# соответствующее сообщение на экран. В противном случае выведите сообщение о том,
# какие символы повторяются. Не используйте множества и подобные структуры данных,
# которые мы пока не изучали, для проверки уникальности символов.

input_string = input("Enter the string: ").lower()
index = 0
unique = True

while index < len(input_string):
    if input_string[index + 1:].find(input_string[index]) != -1:
        unique = False
        print("Symbols aren't unique")
        break
    index += 1

if unique:
    print("Symbols are unique")

# 3. Напишите программу, которая запрашивает у пользователя строку и выравнивает ее по
# центру с заданной шириной. Если строка не может быть выровнена по центру из-за
# нечетной ширины, она должна быть выровне

user_input = input("Enter the string: ")
desired_width = int(input("Enter the width: "))

while desired_width <= len(user_input):
    desired_width = int(input("Width must be greater. Enter width: "))

if len(user_input) % 2 == desired_width % 2:
    aligned_string = user_input.center(desired_width)
else:
    aligned_string = user_input.rjust(desired_width)

print("Result:")
print(aligned_string)
