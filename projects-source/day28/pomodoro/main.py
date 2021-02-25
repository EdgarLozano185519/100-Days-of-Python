# Import screen reader library
import accessible_output2.outputs.auto
from tkinter import *
from sr_label import Sr_Label as sl
from sr_button import Sr_Button as sb

# Initialize screen reader library
s = accessible_output2.outputs.auto.Auto()

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
  window.after_cancel(timer)
  label.config(text="Timer")
  checks.config(text="Pomodoros: 0")
  canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  count = WORK_MIN*60
  label.config(text="Work")
  checks.config(text="Pomodoros: 0")
  reps = 1
  count_down(count, reps)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count, reps):
  if count > 0:
    count -= 1
    global timer
    timer = window.after(1000, count_down, count, reps)
    minutes = count//60
    seconds = count%60
    if minutes < 10: minutes = "0" + str(minutes)
    if seconds < 10: seconds = "0"+str(seconds)
    canvas.itemconfigure(timer_text, text=f"{minutes}:{seconds}")
    #print(count)
  else:
    # Increase reps by 1
    reps += 1
    
    # Update pomodoro count label
    num_checks = reps//2
    checks_text = checkmark*num_checks
    msg = f"Pomodoros: {num_checks} ({checks_text})"
    checks.config(text=msg)
    
    # Handle what timer comes up next: work, short break, or long break
    if reps%8 == 0:
      count = LONG_BREAK_MIN*60
      label.config(text="Long Break", fg=RED)
    elif reps%2 == 0:
      count = SHORT_BREAK_MIN*60
      label.config(text="Short Break", fg=PINK)
    else:
      count = WORK_MIN*60
      label.config(text="Work", fg=GREEN)
    count_down(count, reps)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Set up label
label = sl("Timer")
label.config(
  fg=GREEN,
  font=(FONT_NAME, 50),
  bg=YELLOW
)
label.grid(column=1, row=0)

# Set up canvas
canvas = Canvas(
  width=200,
  height=224,
  takefocus=1,
  bg=YELLOW,
  highlightthickness=0
)
image = PhotoImage("./tomato.png")
canvas.create_image(100, 112, image=image)
def speak_canvas(e):
  s.output(canvas.itemcget(timer_text, 'text'))
canvas.bind('<FocusIn>', speak_canvas)
timer_text = canvas.create_text(
  100,
  130,
  text='00:00',
  fill='white',
  font=(FONT_NAME, 35, 'bold')
)
canvas.grid(column=1, row=1)

# Set up buttons
start = sb("Start", command=start_timer)
reset = sb("Stop", command=reset_timer)
start.grid(column=0, row=2)
reset.grid(row=2, column=2)

# Set up pomodoro count
checkmark = "✓"
checks = sl("Pomodoros: 0")
checks.config(
  fg=GREEN,
  bg=YELLOW
)
checks.grid(column=1, row=3)

# Main loop
window.mainloop()
