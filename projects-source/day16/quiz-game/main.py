import quizzer

quiz = quizzer.Quizzer()

for i in range(10):
  question = quiz.pick_question()
  answer = input(question.question+" (True/False): ").lower()
  if answer == question.correct.lower():
    quiz.right()
    print(f"You are right! Answer is {answer}. {quiz.score}/{quiz.total_questions()}")
  else:
    print(f"You are wrong! Answer is {question.correct}. {quiz.score}/{quiz.total_questions()}")

print("End of game!")
print("You got %d out of 10, giving you  percentage of %.2f" % (quiz.score, (quiz.score/10.0)*100))