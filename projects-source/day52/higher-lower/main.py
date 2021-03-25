from flask import Flask
from random import randint

images = {
  "main": "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif",
  "high": "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif",
  "low": "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif",
  "correct": "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
}
number = randint(0,9)

app = Flask(__name__)

@app.route('/')
def home():
  return f"<h1>Guess a number between 0 and 9</h1> <img alt='home' src={images['main']} />"

@app.route('/guess')
def guess_main():
  return "<p>Please guess a number.</p>"

@app.route('/guess/<int:num>')
def guess(num):
  msg = ""
  if num < number:
    msg += f"<h1>{num} is too low</h1> "
    msg += f"<img alt='low' src={images['low']} />"
  elif num > number:
    msg += f"<h1>{num} is too high</h1> "
    msg += f"<img alt='high' src={images['high']} />"
  else:
    msg += f"<h1>{num} is correct!</h1> "
    msg += f"<img alt='correct' src={images['correct']} />"
  return msg

app.run()