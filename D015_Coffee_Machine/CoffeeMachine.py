from data import resources
from data import MENU
from data import money


def check_ingredients(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            resources[item] -= order_ingredients[item]
            return True

def check_payment():
    """Returns transaction complete if payments are met"""
    print("Please insert coins. ")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    if total >= drink['cost']:
        total -= drink['cost']
        print(f"Here is ${round(total, 2)} in change.")
        print(f"Here is your {choice} ☕️. Enjoy!")
        return True

machine = True
while machine:

    choice = input("What would you like? (espresso ($1.5)/latte ($2.5)/cappuccino ($3)): ").lower()

    if choice == "off":
        machine = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif choice == 'latte' or choice == 'espresso' or choice == 'cappuccino':
        drink = MENU[choice]
        if check_ingredients(drink['ingredients']):
            if check_payment():
                money += drink['cost']
    else:
        print(f"We only serve espresso ($1.5), latte ($2.5), cappuccino ($3) here.")