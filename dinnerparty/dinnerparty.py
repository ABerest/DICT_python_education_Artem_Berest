import random

friends = {}

number = int(input("Enter the number of friends joining :\n"))

if number <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend:")

    for i in range(number):
        name = input()
        friends[name] = 0

    print("Enter the total amount:")
    total = float(input())

    amount = round(total / number, 2)

    for name in friends:
        friends[name] = amount

    print('Do you want to use the "Who is lucky?" Write Yes/No:')
    answer = input()

    if answer == "Yes":
        lucky = random.choice(list(friends.keys()))
        print(f"{lucky} is the lucky one!")
    else:
        print("No one is going to be lucky")