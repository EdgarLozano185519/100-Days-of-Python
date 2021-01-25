# Rock, paper, scissors game
import random

options = ['rock', 'paper', 'scissors']
choice = int(input("Enter 0 for rock, 1 for paper, and 2 for scissors: "))
computer = random.randint(0,2)
you_picked = options[choice]
computer_picked = options[computer]
print("Computer picked "+computer_picked)
if you_picked == 'rock' and computer_picked == "scissors":
  print("You win!")
elif you_picked == 'rock' and computer_picked == "rock":
  print("It's a draw!")
elif you_picked == 'rock' and computer_picked == "paper":
  print("You lose!")
elif you_picked == "paper" and computer_picked == "rock":
  print("You win!")
elif you_picked == "paper" and computer_picked == "paper":
  print("It's a draw!")
elif you_picked == "paper" and computer_picked == "scissors":
  print("You lose!")
elif you_picked == "scissors" and computer_picked == "rock":
  print("You lose!")
elif you_picked == "scissors" and computer_picked == "paper":
  print("You win!")
elif you_picked == "scissors" and computer_picked == "scissors":
  print("It's a draw!")