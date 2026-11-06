
cells = ["_"] * 9

wins = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]


def print_field():
    print("---------")
    for i in range(0, 9, 3):
        print("|", *cells[i:i + 3], "|")
    print("---------")


def check_winner():
    for a, b, c in wins:
        if cells[a] == cells[b] == cells[c] != "_":
            return cells[a]

    if "_" not in cells:
        return "Draw"

    return None


player = "X"
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

    cells[index] = player
    print_field()

    result = check_winner()

    if result == "Draw":
        print("Draw")
        break
    elif result is not None:
        print(f"{result} wins")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"
