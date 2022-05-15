from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu, MenuItem

#TODO 1: Print report.
#TODO 2: Check resources sufficient?
#TODO 3: Process coins.
#TODO 4: Check transaction successful?
#TODO 5: Make coffe.

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}) ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
