from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from speech import s
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake game")
screen.tracer(0)
screen.listen()
snake = Snake()
food = Food()
score = ScoreBoard()

# Keyboard functionality
screen.onkey(score.speak_score, 's')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(food.speak_pos, 'f')

game = True
while game:
  screen.update()
  sleep(0.1)
  snake.move()
  if snake.head.distance(food) < 15:
    s.speak("You ate the food!")
    food.refresh()
    score.increase()
    snake.extend()
  
  # Detect if snake hits wall
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    s.speak("Game over! You crashed into a wall!")
    score.reset()
    snake.reset()
    #game = False
  
  # Detect tail collision
  for segment in snake.segments[1:]:
    if segment.distance(snake.head) < 10:
      s.speak("Your snake is tangled! Game over!")
      score.reset()
      snake.reset()
      #game = False

screen.exitonclick()
