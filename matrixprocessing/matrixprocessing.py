
def read_matrix(name=None):
    if name:
        print(f"Enter size of {name} matrix:")
    else:
        print("Enter matrix size:")

    rows, cols = map(int, input("> ").split())

    if name:
        print(f"Enter {name} matrix:")
    else:
        print("Enter matrix:")

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


def transpose_matrix(matrix, method):
    rows = len(matrix)
    cols = len(matrix[0])

    if method == "1":
        return [list(row) for row in zip(*matrix)]

    elif method == "2":
        if rows != cols:
            return None

        return [list(row) for row in zip(*matrix[::-1])][::-1]

    elif method == "3":
        return [row[::-1] for row in matrix]

    elif method == "4":
        return matrix[::-1]


while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("0. Exit")

    choice = input("Your choice: > ")

    if choice == "0":
        break

    elif choice == "1":
        first = read_matrix("first")
        second = read_matrix("second")
        result = add_matrices(first, second)

    elif choice == "2":
        matrix = read_matrix()
        number = float(input("Enter constant: > "))
        result = multiply_constant(matrix, number)

    elif choice == "3":
        first = read_matrix("first")
        second = read_matrix("second")
        result = multiply_matrices(first, second)

    elif choice == "4":
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")

        method = input("Your choice: > ")

        if method not in ("1", "2", "3", "4"):
            print("Invalid choice!")
            continue

        matrix = read_matrix()
        result = transpose_matrix(matrix, method)

    else:
        print("Invalid choice!")
        continue

    if result is None:
        print("The operation cannot be performed.")
    else:
        show_matrix(result)
