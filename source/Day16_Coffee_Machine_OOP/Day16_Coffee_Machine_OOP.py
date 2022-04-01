# Day 16: Coffee Machine in OOP

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffee_machine():
    menu = Menu()
    cm = CoffeeMaker()
    mm = MoneyMachine()

    order = input(f'What would you like? {menu.get_items()}: ')

    if order == 'off':
        quit()
    elif order == 'report':
        cm.report()
    else:
        item = menu.find_drink(order)

        if item is None:
            quit()
        
        sufficient_resources = cm.is_resource_sufficient(drink=item)

    if sufficient_resources:
        payment_successful = mm.make_payment(cost=item.cost)

        if payment_successful:
            cm.make_coffee(order=item)

if __name__ == '__main__':
    coffee_machine()