
class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550
        self.state = "action"

    def remaining(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def buy(self, choice):
        if choice == "1":
            water = 250
            milk = 0
            coffee = 16
            price = 4

        elif choice == "2":
            water = 350
            milk = 75
            coffee = 20
            price = 7

        elif choice == "3":
            water = 200
            milk = 100
            coffee = 12
            price = 6

        else:
            return

        if self.water < water:
            print("Sorry, not enough water!")
        elif self.milk < milk:
            print("Sorry, not enough milk!")
        elif self.coffee_beans < coffee:
            print("Sorry, not enough coffee beans!")
        elif self.cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= water
            self.milk -= milk
            self.coffee_beans -= coffee
            self.cups -= 1
            self.money += price

    def fill(self):
        self.state = "water"
        print("Write how many ml of water do you want to add:")

    def take(self):
        print(f"I gave you {self.money}")
        self.money = 0

    def process(self, user_input):
        if self.state == "action":
            if user_input == "buy":
                self.state = "buy"
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")

            elif user_input == "fill":
                self.fill()

            elif user_input == "take":
                self.take()

            elif user_input == "remaining":
                self.remaining()

            elif user_input == "exit":
                return False

        elif self.state == "buy":
            if user_input == "back":
                self.state = "action"
            else:
                self.buy(user_input)
                self.state = "action"

        elif self.state == "water":
            self.water += int(user_input)
            self.state = "milk"
            print("Write how many ml of milk do you want to add:")

        elif self.state == "milk":
            self.milk += int(user_input)
            self.state = "coffee"
            print("Write how many grams of coffee beans do you want to add:")

        elif self.state == "coffee":
            self.coffee_beans += int(user_input)
            self.state = "cups"
            print("Write how many disposable cups of coffee do you want to add:")

        elif self.state == "cups":
            self.cups += int(user_input)
            self.state = "action"

        return True


machine = CoffeeMachine()

print("Write action (buy, fill, take, remaining, exit):")

while True:
    user_input = input()
    result = machine.process(user_input)

    if result is False:
        break

    if machine.state == "action":
        print("Write action (buy, fill, take, remaining, exit):")
