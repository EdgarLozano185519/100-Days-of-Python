from turtle import Turtle, Screen, colormode
from random import randint, choice
import colorgram

colors = colorgram.extract('download.jpg', 10)
colors_list = []

print("Colors extracted (rgb values): ")
for color in colors:
  colors_list.append((color.rgb[0], color.rgb[1], color.rgb[2]))

# Handy function to return a random RGB value to be used throughout the program
def generate_rgb():
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)
  return (r, g, b)

#print(generate_rgb())

# Create and configure turtle
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
colormode(255)
# Pen up so lines will not show
timmy_the_turtle.penup()
timmy_the_turtle.hideturtle()
# Adjust turtle to be at a spot
timmy_the_turtle.setheading(225)
timmy_the_turtle.forward(250)

timmy_the_turtle.setheading(90)
timmy_the_turtle.forward(50)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(500)
timmy_the_turtle.right(90)

# Move turtle to draw a shape
#timmy_the_turtle.forward(100)
#timmy_the_turtle.right(90)
#timmy_the_turtle.forward(100)
#timmy_the_turtle.right(90)
#timmy_the_turtle.forward(100)
#timmy_the_turtle.right(90)
#timmy_the_turtle.forward(100)

# Draw alternating line and gap combinations
#for i in range(1,51,2):
#  if i%2 == 0:
#    timmy_the_turtle.pendown()
#    timmy_the_turtle.forward(10)
#  else:
#    timmy_the_turtle.penup()
#    timmy_the_turtle.forward(10)

# Draw dots in different colors in grid fashion
for i in range(1,101):
  timmy_the_turtle.dot(20, choice(colors_list))
  if i%10 == 0:
    timmy_the_turtle.setheading(90)
    timmy_the_turtle.forward(50)
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(500)
    timmy_the_turtle.right(90)
  

# End code to allow window to stay and allow for exit
off_screen= Screen()
off_screen.exitonclick()