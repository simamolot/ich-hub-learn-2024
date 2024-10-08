# Напишите функцию extract_emails(text), которая извлекает все адреса электронной почты из заданного текста и
# возвращает их в виде списка.
# Пример использования:
# text = "Contact us at info@example.com or support@example.com for assistance."
# emails = extract_emails(text)
# print(emails)  # Вывод: ['info@example.com', 'support@example.com']
import re

# def extract_emails(text):
#     pattern = r'\b\w*@\w*\b'
#     return re.findall(pattern, text)
#
#
# text = "Contact us at info@example.com or support@example.com for assistance."
# emails = extract_emails(text)
# print(emails)  # Вывод: ['info@example.com', 'support@example.com']

# Напишите функцию highlight_keywords(text, keywords), которая выделяет все вхождения заданных ключевых слов в тексте,
# окружая их символами *. Функция должна быть регистронезависимой при поиске ключевых слов.
# Пример использования:
# text = "This is a sample text. We need to highlight Python and programming."
# keywords = ["python", "programming"]
# highlighted_text = highlight_keywords(text, keywords)
# print(highlighted_text)
# # Вывод: "This is a sample text. We need to highlight *Python* and *programming*."

import re


def highlight_keywords(text, keywords):
    pattern = '|'.join(map(re.escape, keywords))
    print(pattern)
    highlighted_text = re.sub(pattern, lambda match: f"*{match.group(0)}*", text, flags=re.IGNORECASE)

    return highlighted_text


text = "This is a sample text. We need to highlight Python and programming."
keywords = ["python", "programming"]
highlighted_text = highlight_keywords(text, keywords)
print(highlighted_text)
