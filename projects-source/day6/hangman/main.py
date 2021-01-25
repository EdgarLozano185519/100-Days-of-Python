# Hangman
import random

def check_letter(letter, word, user_word):
  in_word = False
  for char in range(0,len(word)):
    if letter == word[char]:
      in_word = True
      user_word[char] = word[char]
  return in_word

print("Welcome to Hangman!\n\n You have 10 tries to try to guess the word.\n")
words = ['aardvark', 'baboon', 'camel']
word = random.choice(words)
user_word = ['-' for i in range(0,len(word))]
tries = 10
characters_used = []

while tries > 0:
  user = input("Enter a letter: ")
  if user in characters_used:
    print("You already used that letter. Try again.")
    continue
  if check_letter(user, word, user_word):
    print("Good job! That letter is in the word!")
    so_far = "".join(user_word)
    print("Word so far: "+so_far)
  else:
    print("Sorry, that letter is not in the word.")
    tries -= 1
    print("You have " + str(tries) + " tries remaining.")
  characters_used.append(user)
  if word == "".join(user_word):
    print("Good job! You guessed the word!")
    break

if tries == 0:
  print("I'm sorry. You didn't guess the word right.")
  