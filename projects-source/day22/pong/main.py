from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import ScoreBoard

# Setting up screen
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.tracer(0)

# Create paddles
paddle_right = Paddle()
paddle_left = Paddle((-350,0))
# Create ball
ball = Ball()
# Create score board
score = ScoreBoard()

# Screen listening events
screen.listen()
screen.onkey(paddle_right.up, 'Up')
screen.onkey(paddle_right.down, 'Down')
screen.onkey(paddle_left.up, 'w')
screen.onkey(paddle_left.down, 's')

# Main game loop
game_is_running = True
while game_is_running:
  screen.update()
  sleep(0.1)
  ball.move()
  
  # Detect if ball is hitting wall on y-axis
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()
  
  # Detect collision with left and right paddles
  if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
    ball.bounce_x()
  
  # Detect if either side misses
  if ball.xcor() > 380:
    ball.reset()
    ball.bounce_x()
    score.update_right()
  if ball.xcor() < -380:
    ball.reset()
    ball.bounce_x()
    score.update_left()

screen.exitonclick()
