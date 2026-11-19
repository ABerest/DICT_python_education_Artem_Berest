
def read_matrix():
    n, m = map(int, input().split())
    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    return matrix


matrix = read_matrix()
number = int(input())

result = [
    [element * number for element in row]
    for row in matrix
]

for row in result:
    print(*row)
