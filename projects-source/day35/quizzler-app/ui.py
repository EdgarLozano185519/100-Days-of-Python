# Import screen reader library
import accessible_output2.outputs.auto
import tkinter as tk
from sr_label import Sr_Label as sl

# Initialize screen reader library
s = accessible_output2.outputs.auto.Auto()

THEME_COLOR = "#375362"

class QuizInterface:
  def __init__(self, quiz_brain):
    self.quiz = quiz_brain
    # Set up window
    self.window = tk.Tk()
    self.window.title("Quizzler")
    self.window.config(padx=20, pady=20, bg=THEME_COLOR)
    
    # Set up a label for score
    self.score = sl("Score: 0")
    self.score.config(fg="white", bg=THEME_COLOR)
    self.score.grid(row=0, column=1)
    
    # Set up canvas
    self.canvas = tk.Canvas(width=300, height=250, bg='white')
    self.question_text = self.canvas.create_text(
      150,
      125,
      width=280,
      text="Some question text.",
      fill=THEME_COLOR,
      font=("Arial", 20, "italic")
    )
    self.canvas.bind('<FocusIn>', self.speak_question)
    self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
    
    # Buttons
    self.true_image = tk.PhotoImage("images/true.png")
    self.true_button = tk.Button(image=self.true_image, highlightthickness=0, command=self.check_true)
    self.true_button.bind('<FocusIn>', self.speak_true)
    self.true_button.grid(row=2, column=0)
    self.false_image = tk.PhotoImage("images/false.png")
    self.false_button = tk.Button(image=self.false_image, highlightthickness=0, command=self.check_false)
    self.false_button.bind('<FocusIn>', self.speak_false)
    self.false_button.grid(row=2, column=1)
    
    self.get_next_question()
    self.window.mainloop()
  
  def speak_question(self, e):
    text = self.canvas.itemcget(self.question_text, 'text')
    s.output(text)
  
  def speak_true(self, e):
    s.output('True button')
  
  def speak_false(self, e):
    s.output("False button")
  
  def get_next_question(self):
    if self.quiz.still_has_questions():
      self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
    else:
      self.canvas.itemconfig(self.question_text, text="Game Over! Final score shown.")
  
  def check_true(self):
    if self.quiz.current_question.answer == "True" and self.quiz.still_has_questions():
      self.quiz.score += 1
    self.update()
  
  def check_false(self):
    if self.quiz.current_question.answer == "False" and self.quiz.still_has_questions():
      self.quiz.score += 1
    self.update()
  
  def update(self):
    self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
    self.get_next_question()
  
