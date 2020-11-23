from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffee_machine():
    should_run_machine = True
    while should_run_machine:
        myMenu = Menu()
        choice = input(f"What would you like to have? {myMenu.get_items()}: ")
        myMenuItem = myMenu.find_drink(order_name=choice)
        if myMenuItem == None:
            should_run_machine = False
        else:
            maker = CoffeeMaker()
            if maker.is_resource_sufficient:
                myMoneyMachine = MoneyMachine()
                if myMoneyMachine.make_payment(myMenuItem.cost):
                    maker.make_coffee(myMenuItem)
                    print(maker.report())


coffee_machine()