import random

name1 = 'Alex'
name2 = 'Artem'
possible_values = ['1', '2', '3']

while True:
    pencils = input('How many pencils would you like to use:\n')

    if not pencils.isdigit():
        print('The number of pencils should be numeric')
    elif int(pencils) == 0:
        print('The number of pencils should be positive')
    else:
        pencils = int(pencils)
        break

while True:
    first_player = input(f'Who will be the first ({name1}, {name2}):\n')

    if first_player == name1 or first_player == name2:
        break
    else:
        print(f"Choose between '{name1}' and '{name2}'")

while pencils > 0:
    print('|' * pencils)
    print(f"{first_player}'s turn:")

    if first_player == name2:
        if pencils == 1:
            take_pencils = 1
        elif pencils % 4 == 1:
            take_pencils = random.randint(1, 3)
        else:
            take_pencils = (pencils - 1) % 4

        print(take_pencils)

    else:
        while True:
            take_pencils = input()

            if take_pencils not in possible_values:
                print("Possible values: '1', '2' or '3'")
                continue

            take_pencils = int(take_pencils)

            if take_pencils > pencils:
                print("Too many pencils were taken")
                continue

            break

    pencils -= take_pencils

    if pencils == 0:
        if first_player == name1:
            winner = name2
        else:
            winner = name1

        print(f"{winner} won!")
        break

    if first_player == name1:
        first_player = name2
    else:
        first_player = name1
