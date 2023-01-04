MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report(info):
    """prints out resources the machine has"""
    for key in info:
        if key == "coffee":
            print(f"{key}: {info[key]}g")
        elif key == "money":
            print(f"{key}: ${info[key]}")
        else:
            print(f"{key}: {info[key]}ml")


def able(info, choice):
    """checks to see if machine is able to make drink."""
    for key in info:
        if key in choice:
            if info[key] < choice[key]:
                return f"sorry not enough {key}"
    return "go_forth"


def transaction(info, choice):
    """subtracts what is needed to make the drink from machines resources."""
    for key in info:
        if key in choice:
            if info[key] < choice[key]:
                return f"sorry not enough {key}"
            else:
                info[key] -= choice[key]
    return "go_forth"


def payment():
    """Takes coins, adds them up, and returns the value."""
    taken = 0
    quarters = int(input("How many quarters?: ")) * .25
    dimes = int(input("How many dimes?: ")) * .10
    nickles = int(input("How many nickles?: ")) * .05
    pennies = int(input("How many pennies?: ")) * .01
    taken = quarters + dimes + nickles + pennies
    return taken


def paid(held, price):
    """Checks to see if they can pay"""
    if held >= price:
        return
    else:
        return "refunded"


def amount_change(held, price):
    """calculates the change that will be dispensed"""
    if held >= price:
        change = held - price
        return change
    else:
        return held


def coffee_machine():
    """"Coffee machine wrrrmmrmmmmrrrrrrmmm(machine noises)"""
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        print("Machine off")
        return
    elif choice == "report":
        report(resources)
        return coffee_machine()
    choice_ingredients = MENU[choice]["ingredients"]
    choice_price = MENU[choice]["cost"]
    change = 0
    print(f"price ${choice_price}")
    report(resources)
    if able(resources, choice_ingredients) == "go_forth":
        amount = round(payment(), 4)
        if paid(amount, choice_price) == "refunded":
            print("sorry that's not enough money. Money Refunded\n'cling-clang'")
            print(f"dispensed ${amount}")
        else:
            change = amount_change(amount, choice_price)
            resources["money"] += choice_price
            print(f"dispensed ${change}")
            print(f"Here is your {choice}. Enjoy!")
            transaction(resources, choice_ingredients)
    else:
        print(able(resources, choice_ingredients))
        # print(choice_ingredients)
        # print(f"Cost: ${choice_price}")
        # print(MENU[choice])

        # prints out resources
    report(resources)
    return coffee_machine()


resources["money"] = 0
coffee_machine()


