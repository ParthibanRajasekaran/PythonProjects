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

profit=0
is_coffee_machine_on = True

def is_resource_sufficient(drink):
    for item in MENU[drink]['ingredients']:
        if MENU[drink]["ingredients"][item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def inserted_money():
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return round(quarters + dimes + nickles + pennies, 2)

def calculate_cost(drink):
    cost = MENU[drink]["cost"]
    if inserted_money() >= cost:
        return round(inserted_money()-cost,2)
    else:
        print(f"Sorry there is not enough {drink}.")
        return None

def make_coffee(drink):
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]

def process_order(drink):
    global profit
    if is_resource_sufficient(drink):
        payment = inserted_money()
        cost = MENU[drink]['cost']
        if payment >= cost:
            change = round(payment - cost,2)
            profit += change
            make_coffee(drink)
            print(f"Here is ${change} in change.")
            print(f"Here is your {drink}. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")


while is_coffee_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_coffee_machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} ml")
        print(f"Money: $ {profit}")
    elif choice in MENU:
        process_order(drink=choice)
    else:
        print("Sorry, I didn't understand that.")
        is_coffee_machine_on = False