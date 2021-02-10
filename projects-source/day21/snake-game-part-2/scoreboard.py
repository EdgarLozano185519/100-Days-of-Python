from turtle import Turtle
from speech import s

class ScoreBoard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.hideturtle()
    self.color('white')
    self.penup()
    self.goto(0, 270)
    self.update_score()
  
  def speak_score(self):
    s.speak(str(self.score))
  
  def update_score(self):
    self.clear()
    self.write(str(self.score), align="center", font=("Arial", 24, "normal"))
  
  def increase(self):
    self.score += 1
    self.update_score
  
  def game_over(self):
    self.goto(0,0)
    self.write("Game Over", align="center", font=("Arial", 24, "normal"))