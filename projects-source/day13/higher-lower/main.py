from random import randint
from game_data import data

def get_different(num1):
  new = randint(0, len(data)-1)
  while num1 == new:
    new = randint(0, len(data)-1)
  return new

print("Welcome to higher lower, the game to see which influencer has more followers!")
print("You will be given two influencers, or personalities, and you will have to choose which you think has more followers!\n")
correct = True
score = 0
a = randint(0, len(data)-1)
b = get_different(a)
while correct:
  person_a = data[a]["name"]+", a "+data[a]["description"]+", from "+data[a]["country"]+"."
  person_b = data[b]["name"]+", a "+data[b]["description"]+", from "+data[b]["country"]+"."
  print("Compare A: "+person_a)
  print("Compare B: "+person_b)
  choice = input("Who has more followers? Type A or B: ").lower()
  a_count = int(data[a]["follower_count"])
  b_count = int(data[b]["follower_count"])
  answer = max(a_count, b_count)
  if choice == "a" and answer == data[a]["follower_count"]:
    score += 1
    print("You're right! Score: "+str(score))
    b = get_different(a)
  elif choice == "b" and answer == data[b]["follower_count"]:
    score += 1
    print("You're right! Score: "+str(score))
    a = get_different(a)
  else:
    correct = False

print("Sorry, you're wrong. Score: "+str(score))