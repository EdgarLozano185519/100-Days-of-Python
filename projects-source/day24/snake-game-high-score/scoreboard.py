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
    self.high_score = 0
    self.get_high_score()
    self.update_score()
  
  def get_high_score(self):
    with open("data.txt") as file:
      self.high_score = int(file.read())
  
  def speak_score(self):
    s.speak(f"Score: {self.score} high score: {self.high_score}")
  
  def update_score(self):
    self.clear()
    self.write(f"Score: {self.score} high score: {self.high_score}", align="center", font=("Arial", 24, "normal"))
  
  def increase(self):
    self.score += 1
    self.update_score
  
  def reset(self):
    #self.goto(0,0)
    #self.write("Game Over", align="center", font=("Arial", 24, "normal"))
    if self.score > self.high_score:
      self.high_score = self.score
      with open("data", "w") as file:
        file.write(f"{self.score}")
    self.score = 0