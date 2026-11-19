
def read_matrix(name):
    print(f"Enter size of {name} matrix:")
    rows, cols = map(int, input("> ").split())

    print(f"Enter {name} matrix:")
    matrix = []

    for _ in range(rows):
        matrix.append(list(map(float, input("> ").split())))

    return matrix


def show_matrix(matrix):
    print("The result is:")

    for row in matrix:
        print(*[f"{x:g}" for x in row])


def add_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return None

    return [
        [x + y for x, y in zip(row_a, row_b)]
        for row_a, row_b in zip(a, b)
    ]


def multiply_constant(matrix, number):
    return [
        [x * number for x in row]
        for row in matrix
    ]


def multiply_matrices(a, b):
    if len(a[0]) != len(b):
        return None

    columns = list(zip(*b))

    return [
        [sum(x * y for x, y in zip(row, column)) for column in columns]
        for row in a
    ]


while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("0. Exit")

    choice = input("Your choice: > ")

    if choice == "0":
        break

    elif choice == "1":
        first = read_matrix("first")
        second = read_matrix("second")

        result = add_matrices(first, second)

    elif choice == "2":
        matrix = read_matrix("")
        number = float(input("Enter constant: > "))

        result = multiply_constant(matrix, number)

    elif choice == "3":
        first = read_matrix("first")
        second = read_matrix("second")

        result = multiply_matrices(first, second)

    else:
        print("Invalid choice!")
        continue

    if result is None:
        print("The operation cannot be performed.")
    else:
        show_matrix(result)
