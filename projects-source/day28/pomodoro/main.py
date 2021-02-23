# Import screen reader library
import accessible_output2.outputs.auto
from tkinter import *

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

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Set up canvas
canvas = Canvas(width=200, height=224, takefocus=1, bg=YELLOW, highlightthickness=0)
image = PhotoImage("./tomato.png")
canvas.create_image(100, 112, image=image)
def speak_canvas(e):
  s.output("00:00")
canvas.bind('<FocusIn>', speak_canvas)
canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.pack()

# Main loop
window.mainloop()
