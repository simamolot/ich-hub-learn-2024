# 1. Напишите функцию get_response(url), которая отправляет GET-запрос по заданному URL-адресу и возвращает
# объект ответа. Затем выведите следующую информацию об ответе:
# - Код состояния (status code)
# - Текст ответа (response text)
# - Заголовки ответа (response headers)
#
# Пример использования:
# url = "https://api.example.com"
# response = get_response(url)
#
# print("Status Code:", response.status_code)
#
# print("Response Text:", response.text)
#
# print("Response Headers:", response.headers)
# import requests
#
#
def get_response(url):
    response = requests.get(url)
    return f'Status Code: {response.status_code}\nResponse Text: {response.text}\nResponse Headers: {response.headers}\n'


print(get_response('https://lms.itcareerhub.de/'))


def get_response(url):
    try:
        response = requests.get(url)
        return response
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None


url = "https://lms.itcareerhub.de/"
response = get_response(url)
if response is not None:
    print("Status code:", response.status_code)
    print("Response Text:", response.text)
    print("Response Headers:", response.headers)

# 2. Напишите функцию find_common_words(url_list), которая принимает список URL-адресов и возвращает список
# наиболее часто встречающихся слов на веб-страницах. Для каждого URL-адреса функция должна получить содержимое страницы
# с помощью запроса GET и использовать регулярные выражения для извлечения слов. Затем функция должна подсчитать
# количество вхождений каждого слова и вернуть наиболее часто встречающиеся слова в порядке убывания частоты.
from collections import Counter
import re

import requests


def find_common_words(url_list):
    common_word = Counter()

    for url in url_list:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                words = re.findall(r'\b\w+\b', response.text.lower())
                common_word.update(words)
        except requests.RequestException as e:
            print(f'request error {url}: {e}')

    word_counts = Counter(common_word)
    most_common_words = word_counts.most_common()
    return most_common_words


url_list = [
    "https://ilibrary.ru/text/436/p.2/index.html",
    "https://ilibrary.ru/text/69/p.4/index.html"
]
common_words_list = find_common_words(url_list)

print(common_words_list)
