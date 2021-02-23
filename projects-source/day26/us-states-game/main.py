#from speech import s
import accessible_output2.outputs.auto
import turtle
import pandas

s = accessible_output2.outputs.auto.Auto()

def speak_incorrect():
  num_incorrect = len(incorrect)
  num_correct = 50-num_incorrect
  print_string = f"You guessed {num_correct} correct and {num_incorrect} incorrect."
  s.speak(print_string)

# Set up screen
screen = turtle.Screen()
screen.title("U.S. States Game")
# Set up image for turtle shape
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load state data
data = pandas.read_csv("50_states.csv")

# Game
correct = []
incorrect = []
all_states = data.state.to_list()
while len(all_states) < 51:
  title_text = f"{len(correct)}/50 correct; Enter a state: "
  answer = screen.textinput(title=title_text, prompt=title_text).title()
  if answer in all_states:
    correct.append(answer)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state = data[data.state == answer]
    t.goto(int(state.x), int(state.y))
    t.write(state.state, )
  else:
    for state in all_states:
      if state not in correct:
        incorrect.append(state)
    df = pandas.DataFrame(incorrect)
    df.to_csv("incorrect.csv")
    break

screen.listen()
# Keyboard
screen.onkey(speak_incorrect, 's')

# Exit on click
screen.exitonclick()
