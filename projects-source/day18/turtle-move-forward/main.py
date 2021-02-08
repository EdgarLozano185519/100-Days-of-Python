from speech import SpeechSystem
from turtle import Turtle, Screen

def move_forward():
  tim.forward(10)
  s.speak("Moving forward by 10")

s = SpeechSystem(0)
s.speak("testing")

tim = Turtle()
screen = Screen()
screen.listen()
screen.onkey(move_forward, 'space')
screen.exitonclick()