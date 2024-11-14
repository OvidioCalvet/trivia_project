from question_model import Question
from data import question_data

question: list = []

for i in range(0, len(question_data)):

    q = Question(text=question_data[i]['text'], answer= question_data[i]['answer'])

    question.append(q)


