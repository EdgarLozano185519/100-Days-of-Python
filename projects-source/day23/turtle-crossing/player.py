from turtle import Turtle

# Constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
  def __init__(self):
    super().__init__()
    self.shape('square')
    self.color('white')
    self.penup()
    self.goto(STARTING_POSITION)
  
  def move(self):
    self.goto(self.xcor(), self.ycor()+MOVE_DISTANCE)
  
  def is_at_finish_line(self):
    if self.ycor() > FINISH_LINE_Y:
      return True
    return False
  
  def goto_start(self):
    self.goto(STARTING_POSITION)
  