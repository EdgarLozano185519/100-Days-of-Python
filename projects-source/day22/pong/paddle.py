from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, position=(350,0)):
    super().__init__()
    self.shape('square')
    self.shapesize(5, 1)
    self.color('white')
    self.penup()
    self.goto(position[0], position[1])
  
  # Moving functions
  def up(self):
    self.goto(self.xcor(), self.ycor()+20)
  
  def down():
    self.goto(self.xcor(), self.ycor()-20)

    