MENU = {
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
    "money": 0
}

coins = {
    "quarter": 0.25, "dime": 0.10, "nickle": 0.05, "pennie": 0.01
}


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def water(choice):
    return MENU[choice]["ingredients"]["water"]


def milk(choice):
    return MENU[choice]["ingredients"]["milk"]


def coffee(choice):
    return MENU[choice]["ingredients"]["coffee"]


def check_resources(choice):
    resources_ok = True
    choice_water = water(choice)
    choice_milk = milk(choice)
    choice_coffee = coffee(choice)

    resources_water = resources["water"]
    resources_milk = resources["milk"]
    resources_coffee = resources["coffee"]
    if choice_water > resources_water:
        print("Sorry there is not enough water.")
        resources_ok = False
    if choice_milk > resources_milk:
        print("Sorry there is not enough milk.")
        resources_ok = False
    if choice_coffee > resources_coffee:
        print("Sorry there is not enough coffee.")
        resources_ok = False
    return resources_ok


def calc_quarters(amount):
    return amount * coins["quarter"]


def calc_dimes(amount):
    return amount * coins["dime"]


def calc_nickles(amount):
    return amount * coins["nickle"]


def calc_pennies(amount):
    return amount * coins["pennie"]


def get_prize(choice):
    return MENU[choice]["cost"]


def add_money_to_machine(money):
    resources["money"] = resources["money"] + money


def sub_water_from_machine(water):
    resources["water"] = resources["water"] - water


def sub_milk_from_machine(milk):
    resources["milk"] = resources["milk"] - milk


def sub_coffee_from_machine(coffee):
    resources["coffee"] = resources["coffee"] - coffee


def insert_coins(choice):
    not_enough = True
    inserted_money = 0
    while not_enough:
        print("Please insert coins.")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))

        insert_money = inserted_money + calc_quarters(quarters) + calc_dimes(dimes) + calc_nickles(nickles) + \
                       calc_pennies(pennies)

        prize = get_prize(choice)
        print(f"Prize: ${prize}")
        if insert_money >= prize:

            change = insert_money - prize
            if change > 0:
                print(f"Here is ${round(change, 2)} in change.")
            print(f"Here is you're {choice}. Enjoy!")
            add_money_to_machine(prize)
            not_enough = False
        else:
            print(f"Inserted: $round({insert_money},2) - Prize: ${prize}. Sorry that's not enough money. Money refunded.")
            inserted_money = insert_money


power_on = True

while power_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        power_on = False
    elif choice == "report":
        report()

    elif choice == "espresso":
        if check_resources(choice):
            print("Espresso coming")
            insert_coins(choice)
            sub_water_from_machine(water(choice))
            sub_milk_from_machine(milk(choice))
            sub_coffee_from_machine(coffee(choice))
    elif choice == "latte":
        if check_resources(choice):
            print("Latte coming")
            insert_coins(choice)
            sub_water_from_machine(water(choice))
            sub_milk_from_machine(milk(choice))
            sub_coffee_from_machine(coffee(choice))

    elif choice == "cappuccino":
        if check_resources(choice):
            print("Cappuccino coming")
            insert_coins(choice)
            sub_water_from_machine(water(choice))
            sub_milk_from_machine(milk(choice))
            sub_coffee_from_machine(coffee(choice))
