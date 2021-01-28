from os import system, name 

# define our clear function 
def clear():
  if name == 'nt':
    _ = system('cls')
  # for mac and linux(here, os.name is 'posix')
  else:
    _ = system('clear')

dict = {}
while True:
  name_input = input("Enter name: ")
  bid = int(input("Enter bid: "))
  dict[name_input] = bid
  again = input("Are there more people?")
  if again == "yes" or again == "y": clear()
  else: break

if len(dict) <= 1:
  print("Not enough bids.")
else:
  high_bid = 0
  name_string = ""
  for element in dict:
    if dict[element] > high_bid:
      high_bid = dict[element]
      name_string = element
  print(f"Highest bid is {name_string} with a bid of ${high_bid}.")