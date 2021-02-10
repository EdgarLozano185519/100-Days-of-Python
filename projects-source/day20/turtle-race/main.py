from speech import s
from turtle import *
from random import randint

def start():
  for i in range(4):
    turtles[i].penup()
    turtles[i].goto(0, 20*i)
  racing = True
  while racing:
    random_values = [randint(10,30) for i in range(4)]
    for i in range(4):
      turtles[i].forward(random_values[i])
      position = turtles[i].pos()[0]
      if position > 230:
        racing = False
        has_won = colors_list[i]
  s.speak(has_won + " has won the race.")
  if bet.lower() == has_won:
    s.speak("You bet correctly! The turtle you picked won the race!")

def blue_position():
  s.speak("Blue turtle position: " + str(turtles[0].pos()))

def red_position():
  s.speak("Red turtle position: " + str(turtles[1].pos()))

def green_position():
  s.speak("Green turtle position: " + str(turtles[2].pos()))

def yellow_position():
  s.speak("Yellow turtle position: " + str(turtles[3].pos()))

def chose():
  s.speak("You chose " + color)

has_won = "No one "
color = "None"
screen = Screen()
bet = screen.textinput(title="Color Input", prompt="Enter a color of the turtle you think might win: ")
screen.listen()
screen.setup(width=500)
screen.onkey(chose, 'space')

turtles = [Turtle() for i in range(4)]
colors_list = ['blue', 'red', 'green', 'yellow']
for i in range(4):
  turtles[i].goto((0, 20*i))
  turtles[i].color(colors_list[i])
  turtles[i].shape('turtle')

screen.onkey(blue_position, '1')
screen.onkey(red_position, '2')
screen.onkey(green_position, '3')
screen.onkey(yellow_position, '4')
screen.onkey(start, 'r')
screen.exitonclick()
