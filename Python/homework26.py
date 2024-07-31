# 1. Напишите программу, которая принимает в качестве аргумента командной строки путь к файлу .py и запускает его.
# При запуске файла программа должна выводить сообщение "Файл <имя файла> успешно запущен". Если файл не существует
# или не может быть запущен, программа должна вывести соответствующее сообщение об ошибке.

import os
import sys

arg = sys.argv
if len(arg) < 2:
    print('You should setup file name for running in cmd line')
else:
    name_file_for_run = arg[1]
    os.system(f'python {name_file_for_run}')
    print(arg[1])
print('Hello world')

# 2. Напишите программу, которая принимает в качестве аргумента командной строки путь к директории и выводит список
# всех файлов и поддиректорий внутри этой директории. Для этой задачи используйте модуль os и его функцию walk.
# Программа должна выводить полный путь к каждому файлу и директории.


arg = os.walk(input('Enter the list: '))

for i in arg:
    print(i)


