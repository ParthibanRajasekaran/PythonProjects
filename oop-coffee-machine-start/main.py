from CoffeeMachine.main import is_coffee_machine_on
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_coffee_machine_on = True

while is_coffee_machine_on:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    if choice == "off":
        is_coffee_machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)





