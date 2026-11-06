cells = list(input("Enter cells: "))


def print_field():
    print("---------")
    for i in range(0, 9, 3):
        print("|", cells[i], cells[i + 1], cells[i + 2], "|")
    print("---------")


print_field()

while True:
    coordinates = input("Enter the coordinates: ").split()

    try:
        x, y = map(int, coordinates)
    except ValueError:
        print("You should enter numbers!")
        continue

    if not (1 <= x <= 3 and 1 <= y <= 3):
        print("Coordinates should be from 1 to 3!")
        continue

    index = (y - 1) * 3 + (x - 1)

    if cells[index] != "_":
        print("This cell is occupied! Choose another one!")
        continue

    cells[index] = "X"
    break

print_field()