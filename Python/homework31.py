# 1. Напишите декоратор validate_args, который будет проверять типы аргументов функции
# и выводить сообщение об ошибке, если переданы аргументы неправильного типа.
# Декоратор должен принимать ожидаемые типы аргументов в качестве параметров.
# Пример использования:
# @validate_args(int, str)
# def greet(age, name):
#     print(f"Привет, {name}! Тебе {age} лет.")
# greet(25, "Анна")  # Все аргументы имеют правильные типы
# greet("25", "Анна")  # Возникнет исключение TypeError
# Ожидаемый вывод:
# Привет, Анна! Тебе 25 лет.
# TypeError: Аргумент 25 имеет неправильный тип <class 'str'>. Ожидается <class 'int'>.

def validate_args(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, expected_type in zip(args, expected_types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f'Аргумент {arg} не правильного типа {type(arg)}. Нужен {expected_type}')
            return func(*args, **kwargs)

        return wrapper

    return decorator


@validate_args(int, str)
def greet(age, name):
    print(f'Привет {name}! Тебе {age} лет')


greet(25, "Анна")  # Все аргументы имеют правильные типы
greet("25", "Анна")  # Возникнет исключение ValueError

#
#
# 2. Напишите декоратор log_args, который будет записывать аргументы и результаты вызовов функции в лог-файл.
# Каждый вызов функции должен быть записан на новой строке в формате "Аргументы: <аргументы>, Результат: <результат>".
# Используйте модуль logging для записи в лог-файл.
# Пример использования:
# python
# @log_args
# def add(a, b):
#     return a + b
# add(2, 3)
# add(5, 7)
# Ожидаемый вывод в файле log.txt:
# Аргументы: 2, 3, Результат: 5
# Аргументы: 5, 7, Результат: 12
# Убедитесь, что перед запуском кода у вас создан файл log.txt в той же директории, где находится скрипт Python.
import logging


def log_args(func):
    logger = logging.getLogger(func.name)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(r'logging.txt')
    file_handler.setFormatter(logging.Formatter('Аргументы: %(args)s, Результат: %(result)s'))
    logger.addHandler(file_handler)

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info('Аргументы: %s, Результат: %s', args, result)
        return result

    return wrapper


@log_args
def add(a, b):
    add(2, 3)
    add(5, 7)
