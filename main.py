#Anoushka Saha
#Quiz Game
#Main Game
#May 13th, 2024
#Day 17 Final Project

from data import question_data
from question_model import Question

question_bank = []

for question in question_data:
    q_text = question["text"]
    q_ans = question["answer"]
    new_q = Question(q_text, q_ans)
    question_bank.append(new_q)

print(question_bank)


