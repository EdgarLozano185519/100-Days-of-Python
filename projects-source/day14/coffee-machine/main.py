MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
}

print("Welcome to the virtual coffee machine.")
while True:
  choice = input("What would you like? (espresso/latte/cappuccino): ")
  item = MENU[choice]
  ingredients = item["ingredients"]
  
  # First, see if resources exist
  if "water" in ingredients and ingredients["water"] > resources["water"]:
    print("Sorry. Out of water!")
    continue
  elif "milk" in ingredients and ingredients["milk"] > resources["milk"]:
    print("Sorry. Out of milk!")
    continue
  elif "coffee" in ingredients and ingredients["coffee"] > resources["coffee"]:
    print("Sorry. Out of coffee!")
    continue
  
  # Next, ask for quarters, dimes, nickels, and pennies
  quarters = int(input("How many quarters? "))
  dimes = int(input("How many dimes? "))
  pennies = int(input("How many pennies? "))
  nickels = int(input("How many nickels? "))
  total = (quarters*0.25)+(dimes*0.1)+(nickels*0.05)+(pennies*0.01)
  
  # finally, check to see if there is enough money for the coffee
  if total >= item["cost"]:
    print("Here's your coffee. Enjoy!")
    total -= item["cost"]
    resources["water"] -= ingredients["water"]
    resources["coffee"] -= ingredients["coffee"]
    if "milk" in ingredients:
      resources["milk"] -= ingredients["milk"]
    print("Your change is $%.2f " % total)
  else:
    print("Sorry, not enough money.")