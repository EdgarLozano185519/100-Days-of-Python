import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

# Spawn the player
play = Player()
# Init car manager
cars = CarManager()
# Create scoreboard
score = Scoreboard()

# Keyboard functionality
screen.onkey(play.move, 'Up')

game_is_on = True
while game_is_on:
  time.sleep(0.1)
  screen.update()
  cars.move_cars()
  chance = random.randint(1,6)
  if chance == 1:
    cars.create_car()
  if cars.collision(play):
    score.game_over()
    game_is_on = False
  if play.is_at_finish_line():
    play.goto_start()
    cars.level_up()
    score.update_score()

screen.exitonclick()
