
# Підключення модуля для випадкових чисел
import random


# Генерація двох випадкових чисел
num1 = random.randint(2, 9)
num2 = random.randint(2, 9)

# Вибір випадкової арифметичної операції
operation = random.choice(["+", "-", "*"])


# Виведення математичного завдання
print(num1, operation, num2)

# Введення відповіді користувача
answer = int(input("> "))


# Обчислення правильного результату
if operation == "+":
    result = num1 + num2

elif operation == "-":
    result = num1 - num2

else:
    result = num1 * num2


# Перевірка відповіді користувача
if answer == result:
    print("Right!")
else:
    print("Wrong!")
