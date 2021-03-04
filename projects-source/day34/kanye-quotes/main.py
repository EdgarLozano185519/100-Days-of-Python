# Import screen reader library
import accessible_output2.outputs.auto
from tkinter import *
import requests

# Initialize screen reader library
s = accessible_output2.outputs.auto.Auto()

def get_quote():
  response = requests.get('https://api.kanye.rest')
  data = response.json()
  canvas.itemconfig(quote_text, text=data['quote'])

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414, takefocus=1)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
def speak_quote(e):
  s.output(canvas.itemcget(quote_text, 'text'))
canvas.bind('<FocusIn>', speak_quote)
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
def speak_kanye(e):
  s.output("Kanye button")
kanye_button.bind('<FocusIn>', speak_kanye)
kanye_button.grid(row=1, column=0)

window.mainloop()