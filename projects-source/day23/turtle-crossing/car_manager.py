from turtle import Turtle
import random

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
  def __init__(self):
    self.all_cars = []
    self.car_speed = STARTING_MOVE_DISTANCE
  
  def create_car(self):
    new_car = Turtle('square')
    new_car.color('white')
    new_car.shapesize(1, 2)
    new_car.penup()
    new_car.color(random.choice(COLORS))
    position = (300, random.randint(-250, 250))
    new_car.goto(position)
    self.all_cars.append(new_car)
  
  def move_cars(self):
    for car in self.all_cars:
      car.goto(car.xcor()-self.car_speed, car.ycor())
  
  def collision(self, play):
    for car in self.all_cars:
      if car.distance(play) < 20:
        return True
    return False
  
  def level_up(self):
    self.car_speed += MOVE_INCREMENT