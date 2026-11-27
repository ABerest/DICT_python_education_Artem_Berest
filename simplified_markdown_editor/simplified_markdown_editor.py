
# Функція для виведення основ
def show_help():
    # Список усіх доступних форматерів
    print("\nAvailable formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")

    # Спеціальні команди
    print("\nSpecial commands: !help !done")


# Список доступних форматерів Markdown
formatters = [
    "plain",
    "bold",
    "italic",
    "header",
    "link",
    "inline-code",
    "ordered-list",
    "unordered-list",
    "new-line"
]


# Основний цикл програми
while True:

    # Вибір форматера
    command = input("Choose a formatter: ")

    # Введено команду довідки
    if command == "!help":
        show_help()

    # Введено команду завершення програми
    elif command == "!done":
        break

    # Введена команда є у списку форматерів
    elif command in formatters:
        continue

    # Введено невідому команду
    else:
        print("Unknown formatting type or command")
