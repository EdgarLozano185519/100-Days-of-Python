from random import randint

def deal():
  cards = ['ace','2','3','4','5','6','7','8','9','10','king','queen','jack']
  return cards[randint(0, len(cards)-1)]

def calculate(player, card):
  score = player
  if card == 'ace':
    temp_score = score+11
    if temp_score > 21:
      score += 1
    else:
      score += 11
  elif card == 'king' or card == 'queen' or card == 'jack':
    score += 10
  else:
    score += int(card)
  return score

print("Welcome to Black Jack!\n")

dealer_score = 0
player_score = 0

answer = 'y'
while answer == 'y':
  go_again = 'y'
  while player_score < 21 and go_again == 'y':
    player_card = deal()
    print(f"Your card is {player_card}.")
    player_score = calculate(player_score, player_card)
    if dealer_score == 0:
      dealer_card = deal()
      dealer_score = calculate(dealer_score, dealer_card)
      print(f"Dealer's card is {dealer_card}.")
    go_again = input("Do you want another card? Type y or n. ")
  while dealer_score < 17:
    dealer_card = deal()
    dealer_score = calculate(dealer_score, dealer_card)
  print(f"Dealer is done playing. Dealer's final score is {dealer_score}.")
  print(f"Your final score is {player_score}")
  if dealer_score == 21:
    print("The dealer won this match!")
  elif player_score > 21:
    print("You busted! You lose!")
  elif dealer_score > 21:
    print("Dealer busted! You win!")
  elif dealer_score > player_score:
    print("The dealer won this match!")
  elif dealer_score == player_score:
    print("It was a draw!")
  else:
    print("You won! Congratulations!")
  go_again = 'y'
  player_score = 0
  dealer_score = 0
  answer = input("Do you want to play another game? Type y or n.")