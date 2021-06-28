from data import quiz_data

class Question:
  def __init__(self, question_text, question_answer):
    self.question_text = question_text
    self.question_answer = question_answer

class Quiz:
  def __init__(self, questions):
    self.questions = questions
    self.current_score = 0
    self.question_number = 0

  def ask_question(self, question):
    return input(question)

  def has_more_questions(self):
    return self.question_number < len(self.questions)

  def check_for_correctness(self, user_answer, correct_answer):
    if user_answer.strip().lower() == correct_answer.strip().lower():
      self.current_score += 1
      print('correct answer')
    else:
      print("incorrect answer")

    print(f"Correct answer : {correct_answer}")
    print(f"Current score : {self.current_score}")


  def load_next_question(self):
    current_question = self.questions[self.question_number]
    self.question_number += 1
    prepared_question = "Q.{0}:{1}:".format(self.question_number, current_question.question_text)
    user_answer = self.ask_question(prepared_question)
    self.check_for_correctness(user_answer, current_question.question_answer)

def main():
  questions = []
  for question in quiz_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    prepared_question = Question(question_text, question_answer)
    questions.append(prepared_question)
  print("questions are now loaded", questions)

  quiz = Quiz(questions)
  while quiz.has_more_questions():
    quiz.load_next_question()
  print(f"Great attempt! Your final score is {quiz.current_score}")
main()
