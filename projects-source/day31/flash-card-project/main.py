# Import screen reader library
import accessible_output2.outputs.auto
from tkinter import *
from sr_button import Sr_Button as sb
import pandas
import random

# Initialize screen reader library
s = accessible_output2.outputs.auto.Auto()

BACKGROUND_COLOR = "#B1DDC6"

# Flip a card
def flip():
  canvas.itemconfig(canvas_image, image=cardback_image)
  canvas.itemconfig(lang, text='English')
  canvas.itemconfig(word_text, text=word['English'])
  canvas.itemconfig(word_text, fill="white")
  canvas.itemconfig(lang, fill='white')

# Next card function
def next_card():
  global word, timer
  window.after_cancel(timer)
  word = random.choice(data2)
  canvas.itemconfig(canvas_image, image=cardfront_image)
  canvas.itemconfig(word_text, text=word['French'], fill="black")
  canvas.itemconfig(lang, text='French', fill='black')
  timer = window.after(3000, flip)

# Function when getting it right
def right():
  data2.remove(word)
  df = pandas.DataFrame(data2)
  df.to_csv('data/words_to_learn.csv')
  next_card()

# Read CSV data
try:
  data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
  data = pandas.read_csv("data/french_words.csv")
# Convert data to a list of dicts
data2 = data.to_dict(orient="records")
#print(data2)

# Set up window
window = Tk()
window.title("Simple Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Start off timer here
timer = window.after(3000, flip)

# Canvas
canvas = Canvas(
  width=800,
  height=526,
  bg=BACKGROUND_COLOR,
  takefocus=1,
  highlightthickness=0
)
cardfront_image = PhotoImage('images/card_front.png')
cardback_image = PhotoImage('card_back.png')
canvas_image = canvas.create_image(400, 263, image=cardfront_image)
lang = canvas.create_text(
  400,
  150,
  text="title",
  font=("Arial", 40, 'italic')
)
word_text = canvas.create_text(
  400,
  263,
  text="word",
  font=("Ariel", 60, "bold")
)
def speak_canvas(e):
  s.output(canvas.itemcget(lang, 'text')+": "+canvas.itemcget(word_text, 'text'))
canvas.bind('<FocusIn>', speak_canvas)
canvas.grid(row=0, column=0, columnspan=2)

# Button to indicate I don't know word
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = sb("Don't Know", command=next_card)
unknown_button.config(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)

# Button to indicate I know word
check_image = PhotoImage(file="images/right.png")
known_button = sb("Know It", command=right)
known_button.config(image=check_image, highlightthickness=0)
known_button.grid(row=1, column=1)

next_card()

# Main loop
window.mainloop()