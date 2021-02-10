from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]
  
  def create_snake(self):
    for position in STARTING_POSITIONS:
      self.add_seg(position)
  
  def move(self):
    for sn in range(len(self.segments)-1, 0, -1):
      x = self.segments[sn-1].xcor()
      y = self.segments[sn-1].ycor()
      self.segments[sn].goto(x, y)
    self.head.forward(MOVE_DISTANCE)
  
  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)
  
  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)
  
  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
  
  def extend(self):
    self.add_seg(self.segments[-1].pos())
  
  def add_seg(self, position):
    new_seg = Turtle("square")
    new_seg.color("white")
    new_seg.penup()
    new_seg.goto(position)
    self.segments.append(new_seg)
  