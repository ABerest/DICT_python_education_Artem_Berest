pencils = int(input('How many pencils would you like to use:\n'))
name1 = 'Alex'
name2 = 'Artem'
first_player = input (f'Who will be the first ({name1}, {name2}):\n')
while pencils > 0:
    print('|' * pencils)
    print(f"{first_player}'s turn:")
    take_pencils = int(input())
    pencils -= take_pencils
    if pencils == 0:
        break
    else:
        if first_player == name1:
            first_player = name2
        else:
            first_player = name1