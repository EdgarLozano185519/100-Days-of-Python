from random import randint

game = True
tries = 0
difficulty = input('Type "easy" for easy mode or "hard" for hard mode: ')
if difficulty == "easy":
  tries = 10
elif difficulty == "hard":
  tries = 5
else:
  print("That is not a valid option.")

number_to_guess = randint(1,100)
while game and tries > 0:
  guess = int(input("Make a guess: "))
  if number_to_guess == guess:
    print("Horay! You guessed the right number!")
    game = False
  elif guess < number_to_guess:
    print("Your number is too low. Try again.")
    tries -= 1
    print(f"You have {tries} tries remaining.")
  elif guess > number_to_guess:
    print("Your number is too high. Try again.")
    tries -= 1
    print(f"You have {tries} tries remaining.")

if tries == 0:
  print("Sorry. You did not guess the number.")