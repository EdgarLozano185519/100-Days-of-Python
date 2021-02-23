# Import Tkinter library
import tkinter as tk
from sr_button import Sr_Button as sb
from sr_input import Sr_Input as si
from sr_label import Sr_Label as sl

def convert_miles():
  if not input.get().isnumeric():
    label.text = "Invalid Input: Not a number."
  else:
    miles = float(input.get())
    km = miles*1.609344
    label.text = f"Miles: {miles}; kilometers: {km:.2f}"

app = tk.Tk()
app.title("Test")

# Label widget
welcome = sl("Welcome! Convert miles to kilometers here.")
label = sl("Conversion")
welcome.grid()
label.grid()

# Entry widget
input = si("Enter miles:")
input.grid()

# Button widgets
convert = sb(text="Convert", command=convert_miles)
convert.grid()

app.mainloop()
