# Import screen reader library
import accessible_output2.outputs.auto
# Import Tkinter library
import tkinter as tk

# Initialize screen reader library
s = accessible_output2.outputs.auto.Auto()

class Sr_Input(tk.Entry):
  def __init__(self, text=None):
    tk.Entry.__init__(self, text=text)
    self.text = text
    self.bind('<FocusIn>', self.speak_text)
    self.bind('<Key>', self.announce_key)
  
  def speak_text(self, e):
    s.output(self.text+", Editable Text. "+self.get())
  
  def announce_key(self, e):
    s.output(self.get()+e.char)