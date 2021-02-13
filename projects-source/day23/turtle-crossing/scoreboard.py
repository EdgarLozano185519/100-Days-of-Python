from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.level = 1
    self.goto(-280, 260)
    self.level += 1
    self.write(str(self.level), align="left", font=FONT)
  
  def update_level(self):
    self.clear()
    self.level += 1
    self.write(str(level), align="left", font=FONT)
  
  def game_over(self):
    self.goto(0,0)
    self.write("Game Over!", align="center", font=FONT)
  