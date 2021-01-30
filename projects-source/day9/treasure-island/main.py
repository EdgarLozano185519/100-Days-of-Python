print("Welcome to Treasure Island!")
direction = input('You are at a crossroad. Where do you want to go? Type "left" or "right"')
if direction == "right":
  print("You fell into a hole. Game over!")
elif direction == "left":
  print("You've come to a lake. There is an island in the middle of the lake.")
  choice = input('Type "wait" to wait for a boat. Type "swim" to swim across.')
  if choice == "swim":
    print("You get attacked by an angry trout. Game over!")
  elif choice == "wait":
    print("You arrive at the island unharmed. There is a house with three doors. One red, one blue, and one yellow.")
    answer = input("Which do you choose? ")
    if answer == "yellow":
      print("You found the treasure! You win!")
    elif answer == "blue":
      print("You enter a room of beasts! Game over!")
    elif answer == "red":
      print("You enter a room of fire! Game over!")

