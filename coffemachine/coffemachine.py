water = int(input("Write how many ml of water the coffee machine has:\n"))
milk = int(input("Write how many ml of milk the coffee machine has:\n"))
coffee_beans = int(input("Write how many grams of coffee beans the coffee machine has:\n"))

cups = int(input("Write how many cups of coffee you will need:\n"))

water_cups = water // 200
milk_cups = milk // 50
coffee_cups = coffee_beans // 15

max_cups = min(water_cups, milk_cups, coffee_cups)

if max_cups == cups:
    print("Yes, I can make that amount of coffee")
elif max_cups > cups:
    print(f"Yes, I can make that amount of coffee (and even {max_cups - cups} more than that)")
else:
    print(f"No, I can make only {max_cups} cups of coffee")
