class Question:
  def __init__(self, question):
    self.question = question["question"]
    self.category = question["category"]
    self.difficulty = question["difficulty"]
    self.correct = question["correct_answer"]
