import random

print("This is a simple coin toss program.\n\n\n\n")
coin = random.randint(0,1)
if coin == 0:
  print("You got tails.")
else:
  print("You got heads.")