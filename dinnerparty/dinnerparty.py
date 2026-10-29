friends = {}

number = int(input("Enter the number of friends joining :\n"))

if number <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend, each on a new line:")

    for i in range(number):
        name = input()
        friends[name] = 0

    print(friends)