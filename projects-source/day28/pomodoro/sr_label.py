# Import screen reader library
import accessible_output2.outputs.auto
# Import Tkinter library
import tkinter as tk

# Initialize screen reader library
s = accessible_output2.outputs.auto.Auto()

class Sr_Label(tk.Label):
  def __init__(self, text):
    tk.Label.__init__(self, text=text, takefocus=1)
    self.bind('<FocusIn>', self.speak_label)
  
  def speak_label(self, e):
    s.output(self.cget('text'))