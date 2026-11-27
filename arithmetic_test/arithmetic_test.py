import random


# Лічильник правильних відповідей
correct_answers = 0


# Цикл для п'яти завдань
for i in range(5):

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
print(f"Your mark is {correct_answers}/5.")
