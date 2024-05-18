#Anoushka Saha
#Quiz Game
#Main Game
#May 13th, 2024
#Day 17 Final Project

from data import question_data
from question_model import Question
from quizbrain import QuizBrain

#Creating a question bank
question_bank = []
for question in question_data:
    q_text = question["text"]
    q_ans = question["answer"]
    new_q = Question(q_text, q_ans)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.quiz_has_q():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.q_num}")


