LETTERS = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-"
}

print("Welcome to simple string to Morse Code converter.\n")
print("Please enter a string to convert: ")
string = input()
result = ""
for character in string:
    if character == " ":
        result += "  "
    else:
        result += LETTERS[character.lower()]
    result += " "

print(f"The resulting string is:\n{result}")