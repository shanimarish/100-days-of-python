# Day 16 Project: Coffee Machine using OOP

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    user_order = input(f"What would you like? ({options}): ")
    
    if user_order == "off":
        is_on = False
    elif user_order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        chosen_drink = menu.find_drink(user_order)
        
        if coffee_maker.is_resource_sufficient(chosen_drink) and money_machine.make_payment(chosen_drink.cost):
            coffee_maker.make_coffee(chosen_drink)
        