from speech import s
from turtle import *

def clear():
  tim.clear()
  tim.penup()
  tim.home()
  tim.pendown()
  s.speak("Cleared drawing.")

def turn_right():
  tim.right(10)
  s.speak("Turning right.")

def turn_left():
  tim.left(10)
  s.speak("Turning left.")

def move_back():
  tim.back(10)
  s.speak("Moving back 10.")

def speak_pos():
  heading = tim.heading()
  s.speak("Position: " + str(tim.pos()) + " position: " + str(heading))

def move_forward():
  tim.forward(10)
  s.speak("Moved 10 forward.")

#s.speak("hello")
# Define turtle
tim = Turtle()
# Screen functions
screen = Screen()
screen.listen()

onkey(speak_pos, 'space')
onkey(move_forward, 'w')
onkey(move_back, 's')
onkey(turn_right, 'd')
onkey(turn_left, 'a')
onkey(clear, 'c')

#output = textinput(title="Turtle Selector", prompt="Select a turtle you think might win.")
# Exit code
screen.exitonclick()
