from typing import Dict, Union

MENU: Dict[str, Dict[str, Union[Dict[str, int], float]]] = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "Money": 0.0,
}


def print_report():
    print("Water: " + str(resources["water"]))
    print("Milk: " + str(resources["milk"]))
    print("Coffee:" + str(resources["coffee"]))
    print("Money: " + str(resources["Money"]))


def check_resource(type):
    if type == "espresso":
        return resources["water"] > MENU[type]["ingredients"]["water"] and \
               resources["coffee"] > MENU[type]["ingredients"]["coffee"]
    elif type == "latte":
        return resources["water"] > MENU[type]["ingredients"]["water"] and \
               resources["coffee"] > MENU[type]["ingredients"]["coffee"] and \
               resources["coffee"] > MENU[type]["ingredients"]["coffee"]
    elif type == "cappuccino":
        return resources["water"] > MENU[type]["ingredients"]["water"] and \
               resources["coffee"] > MENU[type]["ingredients"]["coffee"] and \
               resources["milk"] > MENU[type]["ingredients"]["milk"]
    else:
        print("Unsupported Type")


def process_coins(type):
    quarters = float(input("Enter quarters: "))
    dimes = float(input("Enter dimes: "))
    nickles = float(input("Enter nickles: "))
    pennies = float(input("Enter pennies: "))
    total_money = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    print("total_money")
    if total_money < MENU[type]["cost"]:
        print("Sorry that's not enough money. Money refunded. ”.")
        return
    elif total_money > MENU["espresso"]["cost"]:
        change_money = total_money - MENU[type]["cost"]
        print(f"Here is the change {change_money}$")
        resources["Money"] += MENU[type]["cost"]
    else:
        resources["Money"] += MENU[type]["cost"]
    resources["water"] -= MENU[type]["ingredients"]["water"]
    resources["milk"] -= MENU[type]["ingredients"]["milk"]
    resources["coffee"] -= MENU[type]["ingredients"]["coffee"]
    print(f"Here is your {type}. Enjoy!")

def coffee_machine():
    should_not_stop = True
    while should_not_stop:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            print("Switching off the Machine for maintainers")
            should_not_stop = False
        elif choice == "Report":
            print_report()
        elif choice == "espresso":
            print("I want espresso")
        elif choice == "latte":
            print("I want latte")
        elif choice == "cappuccino":
            print("I want cappuccino")
        else:
            print("Unsupported Option")

        if choice != "off" and choice != "Report" and check_resource(choice) == True:
            process_coins(choice)


coffee_machine()

