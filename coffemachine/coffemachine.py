water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550


def remaining():
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{coffee_beans} of coffee beans")
    print(f"{cups} of disposable cups")
    print(f"{money} of money")


def buy():
    global water, milk, coffee_beans, cups, money

    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")

    if choice == "back":
        return

    if choice == "1":
        need_water = 250
        need_milk = 0
        need_coffee = 16
        price = 4

    elif choice == "2":
        need_water = 350
        need_milk = 75
        need_coffee = 20
        price = 7

    elif choice == "3":
        need_water = 200
        need_milk = 100
        need_coffee = 12
        price = 6

    else:
        return

    if water < need_water:
        print("Sorry, not enough water!")
    elif milk < need_milk:
        print("Sorry, not enough milk!")
    elif coffee_beans < need_coffee:
        print("Sorry, not enough coffee beans!")
    elif cups < 1:
        print("Sorry, not enough disposable cups!")
    else:
        print("I have enough resources, making you a coffee!")
        water -= need_water
        milk -= need_milk
        coffee_beans -= need_coffee
        cups -= 1
        money += price


def fill():
    global water, milk, coffee_beans, cups

    water += int(input("Write how many ml of water do you want to add:\n"))
    milk += int(input("Write how many ml of milk do you want to add:\n"))
    coffee_beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
    cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))


def take():
    global money

    print(f"I gave you {money}")
    money = 0

while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")

    if action == "buy":
        buy()

    elif action == "fill":
        fill()

    elif action == "take":
        take()

    elif action == "remaining":
        remaining()

    elif action == "exit":
        break
