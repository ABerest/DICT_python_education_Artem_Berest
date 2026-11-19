
def read_matrix():
    rows, cols = map(int, input().split())
    matrix = []

    for _ in range(rows):
        matrix.append(list(map(int, input().split())))

    return matrix


matrix_a = read_matrix()
matrix_b = read_matrix()

if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
    print("ERROR")
else:
    result = []

    for row_a, row_b in zip(matrix_a, matrix_b):
        new_row = [a + b for a, b in zip(row_a, row_b)]
        result.append(new_row)

    for row in result:
        print(*row)
