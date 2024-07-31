# Напишите программу, которая принимает список слов от пользователя и использует генераторное выражение
# (comprehension) для создания нового списка, содержащего только те слова, которые начинаются с гласной буквы.
# Затем программа должна использовать функцию map, чтобы преобразовать каждое слово в верхний регистр. В результате
# программа должна вывести новый список, содержащий только слова, начинающиеся с гласной буквы и записанные в верхнем
# регистре.

list_laters = ['a', 'o', 'y', 'i', 'u']
list_words = ['appel', 'orange', 'yellow', 'igloo', 'ugo']
list_comprehension = [word for word in list_words if word.lower()[0] in list_laters]
func_comprehension = list(map(str.upper, list_comprehension))

print(list_comprehension)
print(func_comprehension)

# Напишите программу, которая принимает список чисел от пользователя и использует функцию reduce из модуля functools,
# чтобы найти произведение всех чисел в списке. Затем программа должна использовать функцию itertools.accumulate для
# накопления произведений чисел в новом списке. В результате программа должна вывести список, содержащий накопленные
# произведения.

from functools import reduce
from itertools import accumulate

numbers = [1, 2, 3, 4, 5, 6]
result = reduce(lambda x, y: x * y, numbers)
print(result)
result_2 = list(accumulate(numbers, lambda x, y: x * y))
print(result_2)

