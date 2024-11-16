from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank: list = []

for question in question_data:

    question_text: str = question['text']
    question_answer: str = question['answer']

    new_question = Question(question_text, question_answer)

    question_bank.append(new_question)

quiz: object = QuizBrain(question_bank)

while quiz.still_has_questions(): quiz.next_question()

print('\n')
print(f'You have completed the quiz! Your score was {quiz.score} / {quiz.question_number}')