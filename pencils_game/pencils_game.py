while True:
    pencils = input('How many pencils would you like to use:\n')
    if pencils == '0':
        print('The number of pencils should be positive')
    elif pencils.isdigit():
        pencils = int(pencils)
        break
    else:
        print('The number of pencils should be numeric')
name1 = 'Alex'
name2 = 'Artem'
possible_values = ['1', '2', '3']
while True:
    first_player = input(f'Who will be the first ({name1}, {name2}):\n')
    if first_player == name1 or first_player == name2:
        break
    else:
        print(f"Choose between '{name1}' and '{name2}'")
while pencils > 0:
    print('|' * pencils)
    print(f"{first_player}'s turn:")
    while True:
        take_pencils = input()
        if take_pencils in possible_values:
            if int(take_pencils) <= pencils:
                break
            else:
                print("Too many pencils were taken")
        else:
            print("Possible values: '1', '2' or '3'")

    pencils -= int(take_pencils)
    if pencils == 0:
        if first_player == name1:
            winner = name2
        else:
            winner = name1
        print(f"{winner} won!")
        break
    else:
        if first_player == name1:
            first_player = name2
        else:
            first_player = name1
