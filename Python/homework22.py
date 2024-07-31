# 1. Напишите программу, которая открывает файл, считывает из него два числа и выполняет операцию их деления.
# Если число отрицательное, выбросите исключение ValueError с
# сообщением "Число должно быть положительным". Обработайте исключение и выведите соответствующее сообщение.


def file_1(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            num1, num2 = map(float, file.read().strip().split())
            if num1 < 0 or num2 < 0:
                raise ValueError('Число должно быть положительным')

            result = num1 / num2
        return result
    except ValueError as value:
        return f"Error: {value}"
    except FileNotFoundError as fe:

        print(f'{fe} was not found ')


file_name = 'probe.txt1'
print(file_1(file_name))


# 2. Напишите программу, которая открывает файл, считывает его содержимое и выполняет операции над числами в файле.
# Обработайте возможные исключения при открытии файла (FileNotFoundError)
# и при выполнении операций над числами (ValueError, ZeroDivisionError). Используйте конструкцию try-except-finally для
# обработки исключений и закрытия файла в блоке finally.


def read_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            num1, num2 = map(float, file.readline().split())
            result = num1 / num2
            print(f'Результат деления: {result:.2f}')
    except FileNotFoundError:
        print(f'Файл "{filename}" не найден.')
    except ZeroDivisionError:
        print('Деление на ноль недопустимо.')
    except ValueError:
        print('Ошибка: Неверный формат данных в файле.')
    finally:
        print('Выполнение завершено, файл закрыт (если был открыт).')


filename = 'probe.txt'
read_numbers_from_file(filename)
