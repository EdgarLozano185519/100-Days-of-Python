from turtle import Turtle
from random import randint
from speech import s

class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.shapesize(0.5, 0.5)
    self.color('blue')
    self.speed('fastest')
    self.refresh()
  
  def speak_pos(self):
    s.speak(str(self.x) + " " + str(self.y))
  
  def refresh(self):
    self.x = randint(-280, 280)
    self.y = randint(-280, 280)
    self.goto(self.x, self.y)