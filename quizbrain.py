#Anoushka Saha
#Quiz Game
#Quiz Brain Object
#May 18th, 2024
#Day 17 Final Project

class QuizBrain:
    def __init__(self, q_list):
        self.q_num = 0
        self.score = 0
        self.q_list = q_list

    def quiz_has_q(self):
        return self.q_num < len(self.q_list)
    
    def next_question(self):
        current_q = self.q_list[self.q_num]
        self.q_num += 1
        user_ans = input(f"Q.{self.q_num}: {current_q.text} (True/False): ")
        self.check_answer(user_ans, current_q.answer)

    def check_answer(self, user_ans, correct_answer):
        if user_ans.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.q_num}")
        print("\n")
