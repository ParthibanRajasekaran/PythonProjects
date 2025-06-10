class QuizBrain:

    def __init__(self, questions_list):
        self.questions_number = 0
        self.questions_list = questions_list
        self.score=0

    def still_has_questions(self):
        return self.questions_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.questions_number]
        self.questions_number += 1
        user_answer = input(f"Q.{self.questions_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Got got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your score is: {self.score}/{self.questions_number}")