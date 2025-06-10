from question_model import Question
from open_trivia_data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]

    question = Question(text, answer)
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz_brain.score} / {quiz_brain.questions_number}")


