import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
codes = {row.letter : row.code for (index, row) in data.iterrows()}
#print(dict1)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user = input("Enter word to be converted to phoenetic codes: ").upper()

while True:
  try:
    phon_list = [codes[char] for char in user]
  except KeyError:
    print("Enter only letters please.")
    user = input("Enter word to be converted to phoenetic codes: ").upper()
  else:
    break

phon_list = [codes[char] for char in user]
print(phon_list)