from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
# menu_item = MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    items = menu.get_items()
    order = input(f"Either wanna report or !What would you like? {items}: ")

    if order == "off":
        is_on = False

    elif order == "report":
        money_machine.report()
        coffee_maker.report()

    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)





