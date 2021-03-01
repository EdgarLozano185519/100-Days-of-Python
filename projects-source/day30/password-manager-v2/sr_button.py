# Import screen reader library
import accessible_output2.outputs.auto
# Import Tkinter library
import tkinter as tk

# Initialize screen reader library
s = accessible_output2.outputs.auto.Auto()

class Sr_Button(tk.Button):
  def __init__(self, text=None, command=None):
    super().__init__(text=text, command=command)
    self.text = text
    self.bind('<FocusIn>', self.speak_text)
  
  def speak_text(self, e):
    s.output(self.text+" button")