cells = input("Enter cells: ")

print("---------")

for i in range(0, 9, 3):
    print("|", cells[i], cells[i + 1], cells[i + 2], "|")

print("---------")

x_count = cells.count("X")
o_count = cells.count("O")

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

x_wins = False
o_wins = False

for a, b, c in wins:
    if cells[a] == cells[b] == cells[c]:
        if cells[a] == "X":
            x_wins = True
        elif cells[a] == "O":
            o_wins = True

if abs(x_count - o_count) >= 2 or (x_wins and o_wins):
    print("Impossible")
elif x_wins:
    print("X wins")
elif o_wins:
    print("O wins")
elif "_" in cells:
    print("Game not finished")
else:
    print("Draw")
