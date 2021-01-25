# Simple password generator
import random

print("Welcome to the simplest password generator of all time!\n")
print("Enter the requested information, and make sure to note the resulting password at the end.\n\n")
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
how_many_letters = int(input("How many letters in the password? "))
numbers = ['0','1','2','3','4','5','6','7','8','9']
how_many_numbers = int(input("How many digits? "))
symbols = ['!','@','$','%']
how_many_symbols = int(input("How many symbols?"))

password = ""
letter_counter = 0
while letter_counter < how_many_letters:
  choice = random.randint(0,25)
  password += letters[choice]
  letter_counter += 1

number_counter = 0
while number_counter < how_many_numbers:
  choice = random.randint(0,9)
  password += numbers[choice]
  number_counter += 1

symbol_counter = 0
while symbol_counter < how_many_symbols:
  choice = random.randint(0,len(symbols)-1)
  password += symbols[choice]
  symbol_counter += 1

print("Your password is " + password)