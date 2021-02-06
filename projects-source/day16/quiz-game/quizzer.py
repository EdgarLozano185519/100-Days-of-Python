from data import data
from random import randint
from question import Question

class Quizzer:
  def __init__(self):
    self.data = data["results"]
    self.questions = []
    self.score = 0
    self.current = None
  
  def question_already_picked(self, qid):
    for id in self.questions:
      if id == qid:
        return True
    return False
  
  def pick_question(self):
    """Returns a question from the list"""
    question_id = randint(0, 49)
    while self.question_already_picked(question_id):
      question_id = randint(0, 49)
    self.questions.append(question_id)
    question = Question(self.data[question_id])
    self.current = question
    return question
  
  def right(self):
    self.score += 1
  
  def total_questions(self):
    return len(self.questions)