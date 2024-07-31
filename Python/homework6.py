# Напишите программу, которая генерирует случайное число от 1 до 100, а затем предлагает пользователю угадать это число.
# Если пользователь угадывает число, программа выводит сообщение о победе.
# Если пользователь не угадывает число, программа сообщает,
# больше или меньше загаданное число и предлагает попробовать снова.
# Используйте цикл с инструкцией break, чтобы остановить выполнение цикла, когда число угадано.

secret_number = 54

print("Guess the number between 1 and 100:")

while True:
    guess = int(input("Your guess: "))

    if guess < secret_number:
        print("The secret number is higher.")
    elif guess > secret_number:
        print("The secret number is lower.")
    else:
        print(f"Congratulations! You guessed the number {secret_number}!")
        break
print(f"The exact secret number was: {secret_number}")


# 2. Напишите программу, которая запрашивает у пользователя число N и выводит первые N чисел Фибоначчи.
# Числа Фибоначчи - это последовательность чисел, где каждое следующее число является суммой двух предыдущих
# чисел (начиная с 0 и 1). Используйте цикл
# while для решения задачи. Выведите числа через запятую с помощью команды print.

number_1 = int(input("Enter the number: "))
number_2 = 2

while number_2 < number_1:
    if number_1 % number_2 == 0:
        print("This number is not prime.")
        break
    number_2 += 1
else:
    print("This number is prime.")
