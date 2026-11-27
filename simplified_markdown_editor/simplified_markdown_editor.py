
# Функція для виведення довідки
def show_help():
    # Список усіх доступних форматерів
    print("\nAvailable formatters: plain, bold, italic, header, link, inline-code, ordered-list, unordered-list, new-line")

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


# Змінна для збереження Markdown
markdown = ""


# Основний цикл програми
while True:

    # Вибір форматера
    command = input("Choose a formatter: ")

    # Введено команду довідки
    if command == "!help":
        show_help()
        continue

    # Введено команду завершення програми
    elif command == "!done":

        # Збереження Markdown у файл
        with open("output.md", "w", encoding="utf-8") as file:
            file.write(markdown)

        break

    # Введено невідому команду
    elif command not in formatters:
        print("Unknown formatting type or command")
        continue

    # Введено команду нового рядка
    elif command == "new-line":
        markdown += "\n"

    # Введено форматер заголовка
    elif command == "header":

        # Вибір рівня заголовка
        level = int(input("Level: "))

        # Перевірка рівня заголовка
        if level < 1 or level > 6:
            print("The level should be within the range of 1 to 6.")
            continue

        # Введення тексту заголовка
        text = input("Text: ")

        # Додавання заголовка до Markdown
        markdown += "#" * level + " " + text + "\n"

    # Введено форматер посилання
    elif command == "link":

        # Введення назви посилання
        label = input("Label: ")

        # Введення URL посилання
        url = input("URL: ")

        # Додавання посилання до Markdown
        markdown += "[" + label + "]("'https://' + url + ")\n"

    # Введено форматер списку
    elif command == "ordered-list" or command == "unordered-list":

        # Введення кількості рядків
        rows = int(input("Number of rows: "))

        # Перевірка кількості рядків
        while rows <= 0:
            print("The number of rows should be greater than zero")
            rows = int(input("Number of rows: "))

        # Додавання елементів списку
        for i in range(1, rows + 1):

            # Введення елемента списку
            text = input(f"Row #{i}: ")

            # Додавання елемента нумерованого списку
            if command == "ordered-list":
                markdown += f"{i}. {text}\n"

            # Додавання елемента ненумерованого списку
            else:
                markdown += f"* {text}\n"

    # Введено інший форматер
    else:

        # Введення тексту
        text = input("Text: ")

        # Звичайний текст
        if command == "plain":
            markdown += text + "\n"

        # Напівжирний текст
        elif command == "bold":
            markdown += "**" + text + "**\n"

        # Курсивний текст
        elif command == "italic":
            markdown += "*" + text + "*\n"

        # Вбудований код
        elif command == "inline-code":
            markdown += "`" + text + "`\n"

    # Виведення всієї Markdown-розмітки
    print(markdown, end="")
