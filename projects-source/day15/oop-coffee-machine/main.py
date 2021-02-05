from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
mm = MoneyMachine()
menu = Menu()

print("Welcome to the virtual coffee machine!")
while True:
  prompt = "Type your choice. ("+menu.get_items() + "): "
  choice = input(prompt)
  item = menu.find_drink(choice)
  if item == None:
    continue
  sufficient = maker.is_resource_sufficient(item)
  if not sufficient:
    mm.report()
    break
  payment = mm.make_payment(item.cost)
  if not payment:
    continue
  maker.make_coffee(item)
  mm.report()