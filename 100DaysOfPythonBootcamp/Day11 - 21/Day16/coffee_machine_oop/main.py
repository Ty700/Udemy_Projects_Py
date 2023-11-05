#Other files I didn't write. I am to read the documentation of how the coffee_machine/maker/etc classes work and do something with it.
#Pretending it's an external lib I have imported
#This exercise is to show how OOP makes it much easier and readable through abstraction

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from clear import clear

clear()

isOn = True

menu = Menu()
maker = CoffeeMaker()
moneyHandler = MoneyMachine()

while(isOn):
    selectionText = "What would you like: " + menu.get_items()
    coffeeSelection = input(f"{selectionText}\n")

    if(coffeeSelection.lower() == "off"):
        print("Shutting Down...")
        isOn = False
        break
    elif(coffeeSelection.lower() == "report"):
        maker.report() #resources
        moneyHandler.report() #profit
        continue

    coffeeToMake = menu.find_drink(coffeeSelection.lower())

    if(coffeeToMake != None):
        if(maker.is_resource_sufficient(coffeeToMake)):
            print("Total: ${:.2f}".format(coffeeToMake.cost))
            if(moneyHandler.make_payment(coffeeToMake.cost)):
                maker.make_coffee(coffeeToMake)
                