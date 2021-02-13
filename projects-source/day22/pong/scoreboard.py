from turtle import Turtle

class ScoreBoard(Turtle):
  def __init__(self):
    super().__init__()
    self.color('white')
    self.penup()
    self.hideturtle()
    self.l_score = 0
    self.r_score = 0
    
  def update_left(self):
    self.goto(-100, 200)
    self.clear()
    self.l_score += 1
    self.write(str(self.l_score), align="center", font=("Courier", 80, "normal"))
  
  def update_right(self):
    self.goto(100, 200)
    self.clear()
    self.r_score += 1
    self.write(str(self.r_score), align="center", font=("Courier", 80, "normal"))
  