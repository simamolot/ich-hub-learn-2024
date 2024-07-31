# Напишите программу, которая принимает список слов и возвращает список, содержащий только анаграммы.
# Анаграммы - это слова, составленные из одних и тех же букв, но в разном порядке.
# Создайте функцию anagrams, которая принимает список слов в качестве аргумента и возвращает список анаграмм.
# Используйте множества и сортировку букв в слове для проверки на анаграмму. Выведите результат на экран.
# Пример переданного списка слов:
# ['cat', 'dog', 'tac', 'god', 'act']
# Пример вывода:
# Анаграммы: ['dog', 'god'], ['cat', 'tac', 'act']

a = ['cat', 'dog', 'tac', 'god', 'act', 'bober', 'top']


def return_anagram_dict(words: list[str]):
    anagram_dict = dict()
    words = [(word, ''.join(sorted(list(word)))) for word in words]
    for item in words:
        if item[1] not in anagram_dict:
            anagram_dict.update({item[1]: [item[0]]})
        else:
            anagram_dict[item[1]].append(item[0])
    return [value for value in anagram_dict.values() if len(value) > 1]


print(return_anagram_dict(a))


# Напишите функцию is_subset, которая принимает два множества set1 и set2 и проверяет,
# является ли set1 подмножеством set2. Функция должна возвращать True, если все элементы из set1 содержатся в set2,
# и False в противном случае. Функция должна быть реализована без использования встроенных методов issubset или <=.
# Пример ножеств
#
# {1, 2, 3}
# {1, 2, 3, 4, 5}
# Пример вывода:
# True

def is_subset(set1, set2):
    for elem in set1:
        if elem not in set2:
            return False
    return True


set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(is_subset(set1, set2))
