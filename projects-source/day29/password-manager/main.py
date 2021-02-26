# Imports
import random
# Import screen reader library
import accessible_output2.outputs.auto
# tkinter imports
from tkinter import *
from sr_label import Sr_Label as sl
from sr_input import Sr_Input as si
from sr_button import Sr_Button as sb
from tkinter import messagebox
# Import pyperclip to deal with clipboard
import pyperclip

# Initialize screen reader library
s = accessible_output2.outputs.auto.Auto()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
  # Characters list
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
  # Random numbers for different types of chars
  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)
  # Empty list
  password_list = []
  # Add from character lists using list comprehension
  password_list += [random.choice(letters) for char in range(nr_letters)]
  password_list += [random.choice(symbols) for char in range(nr_symbols)]
  password_list += [random.choice(numbers) for char in range(nr_numbers)]
  random.shuffle(password_list)
  password = "".join(password_list)
  return password

# Password function tied to generate button
def generate_password_button():
  password_input.delete(0,len(password_input.get()))
  password = password_generate()
  password_input.insert(0, password)
  pyperclip.copy(password)
  messagebox.showinfo(
    title="Alert",
    message="Password copied to clipboard and password field populated."
  )
  

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
  temp_email = email_input.get()
  temp_password = password_input.get()
  temp_website = website_input.get()
  if len(temp_email) == 0 or len(temp_website) == 0 or len(temp_password) == 0:
    messagebox.showinfo(
      title="Error!",
      message="Please make sure all fields are filled out."
    )
  else:
    ask = messagebox.askokcancel(
      title=f"{temp_website}",
      message=f"These are the details:\nWebsite: {temp_website}\nEmail: {temp_email}\nPassword: {temp_password}\nIs it ok to save?"
    )
    if ask:
      with open("data.txt", "a") as file:
        line = f"{temp_website}|{temp_email}|{temp_password}\n"
        file.write(line)
      website_input.delete(0,len(website_input.get()))
      email_input.delete(0,len(email_input.get()))
      password_input.delete(0,len(password_input.get()))
      website_input.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Set up canvas
canvas = Canvas(height=200, width=200, takefocus=1)
image = PhotoImage('logo.png')
canvas.create_image(100, 100, image=image)
def speak_canvas(e):
  s.output("logo")
canvas.bind('<FocusIn>', speak_canvas)
canvas.grid(column=1, row=0)

# Labels
website = sl("Website")
website.config(takefocus=0)
website.grid(column=0, row=1)
email = sl("Email")
email.config(takefocus=0)
email.grid(column=0, row=2)
password = sl("Password")
password.config(takefocus=0)
password.grid(column=0, row=3)

# Entries
website_input = si("Website:")
website_input.config(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
email_input = si("Email:")
email_input.config(width=35)
email_input.grid(column=1, row=2, columnspan=2)
password_input = si("Password:")
password_input.config(width=21)
password_input.grid(column=1, row=3)

# Buttons
generate_password = sb(text="Generate Password", command=generate_password_button)
generate_password.grid(row=3, column=2)
add_button = sb(text="Add", command=save_to_file)
add_button.config(width=36)
add_button.grid(row=4, column=1, columnspan=2)

# main loop
window.mainloop()