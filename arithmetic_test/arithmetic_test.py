
# Підключення модуля для випадкових чисел
import random


# Вибір рівня складності
while True:
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")

    # Введення рівня складності
    try:
        level = int(input("> "))

        # Перевірка вибраного рівня
        if level == 1 or level == 2:
            break
        else:
            print("Incorrect format.")

    # Обробка неправильного введення
    except ValueError:
        print("Incorrect format.")


# Лічильник правильних відповідей
correct_answers = 0


# Цикл для п'яти завдань
for i in range(5):

    # Генерація завдання для першого рівня
    if level == 1:

        # Генерація двох випадкових чисел
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)

        # Вибір випадкової арифметичної операції
        operation = random.choice(["+", "-", "*"])

        # Виведення математичного завдання
        print(num1, operation, num2)

        # Обчислення правильного результату
        if operation == "+":
            result = num1 + num2

        elif operation == "-":
            result = num1 - num2

        else:
            result = num1 * num2

    # Генерація завдання для другого рівня
    else:

        # Генерація випадкового числа
        num = random.randint(11, 29)

        # Обчислення квадрата числа
        result = num ** 2

        # Виведення математичного завдання
        print(num)

    # Введення та перевірка відповіді
    while True:
        try:
            answer = int(input("> "))
            break

        # Обробка неправильного формату відповіді
        except ValueError:
            print("Incorrect format.")

    # Перевірка відповіді користувача
    if answer == result:
        print("Right!")
        correct_answers += 1

    else:
        print("Wrong!")


# Виведення результату після п'яти завдань
print(f"Your mark is {correct_answers}/5. Would you like to save the result? Enter yes or no.")

# Запит на збереження результату
save = input("> ")


# Перевірка відповіді користувача
if save.lower() in ["yes", "y"]:

    # Введення імені користувача
    print("What is your name?")
    name = input("> ")

    # Визначення опису рівня складності
    if level == 1:
        description = "simple operations with numbers 2-9"
    else:
        description = "integral squares of 11-29"

    # Збереження результату у файл
    with open("results.txt", "a", encoding="utf-8") as file:
        file.write(f"{name}: {correct_answers}/5 in level {level} ({description}).\n")

    # Повідомлення про збереження
    print('The results are saved in "results.txt".')
