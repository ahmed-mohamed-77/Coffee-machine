from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()



# the off method
is_on = True

while is_on:
    # ask the user what he wants to drink
    choice = input(f"What would you like? {menu.get_items()}: ".title()).strip().lower()
    list_menu = menu.get_items().split("/")
    list_menu.pop(-1)

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    elif choice == "menu":
        print(" ".join(list_menu))
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink=drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)




print("*" * 30)
