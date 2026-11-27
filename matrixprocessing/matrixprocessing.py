
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
        print(*[f"{x:.2f}".rstrip("0").rstrip(".") for x in row])


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


def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        return None

    data = [row[:] for row in matrix]
    size = len(data)
    result = 1

    for i in range(size):
        pivot = max(range(i, size), key=lambda r: abs(data[r][i]))

        if abs(data[pivot][i]) < 1e-10:
            return 0

        if pivot != i:
            data[i], data[pivot] = data[pivot], data[i]
            result *= -1

        value = data[i][i]
        result *= value

        for j in range(i + 1, size):
            factor = data[j][i] / value

            for k in range(i, size):
                data[j][k] -= factor * data[i][k]

    return result


def inverse_matrix(matrix):
    size = len(matrix)

    if size != len(matrix[0]):
        return None

    left = [row[:] for row in matrix]
    right = [
        [1.0 if i == j else 0.0 for j in range(size)]
        for i in range(size)
    ]

    for i in range(size):
        pivot = max(range(i, size), key=lambda r: abs(left[r][i]))

        if abs(left[pivot][i]) < 1e-10:
            return None

        left[i], left[pivot] = left[pivot], left[i]
        right[i], right[pivot] = right[pivot], right[i]

        divider = left[i][i]

        left[i] = [x / divider for x in left[i]]
        right[i] = [x / divider for x in right[i]]

        for j in range(size):
            if j == i:
                continue

            factor = left[j][i]

            left[j] = [
                x - factor * y
                for x, y in zip(left[j], left[i])
            ]

            right[j] = [
                x - factor * y
                for x, y in zip(right[j], right[i])
            ]

    return right


while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")

    choice = input("Your choice: > ")

    if choice == "0":
        break

    elif choice == "1":
        first = read_matrix("first")
        second = read_matrix("second")
        result = add_matrices(first, second)

        if result is None:
            print("The operation cannot be performed.")
        else:
            show_matrix(result)

    elif choice == "2":
        matrix = read_matrix()
        number = float(input("Enter constant: > "))
        result = multiply_constant(matrix, number)
        show_matrix(result)

    elif choice == "3":
        first = read_matrix("first")
        second = read_matrix("second")
        result = multiply_matrices(first, second)

        if result is None:
            print("The operation cannot be performed.")
        else:
            show_matrix(result)

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

        if result is None:
            print("The operation cannot be performed.")
        else:
            show_matrix(result)

    elif choice == "5":
        matrix = read_matrix()
        result = determinant(matrix)

        if result is None:
            print("The operation cannot be performed.")
        else:
            print("The result is:")
            print(f"{result:.2f}".rstrip("0").rstrip("."))

    elif choice == "6":
        matrix = read_matrix()
        result = inverse_matrix(matrix)

        if result is None:
            print("This matrix doesn't have an inverse.")
        else:
            show_matrix(result)

    else:
        print("Invalid choice!")
