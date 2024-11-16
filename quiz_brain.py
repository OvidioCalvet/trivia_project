class QuizBrain():

    def __init__(self, question_list):

        self.score: int = 0
        self.question_number: int = 0
        self.question_list = question_list

    def still_has_questions(self):

        return self.question_number < len(self.question_list)

    def next_question(self):

        current_question = self.question_list[self.question_number]

        self.question_number += 1

        response: str = input(f'Question {self.question_number}: {current_question.text} (TRUE/FALSE)?: ')

        self.check_answer(response, current_question.answer)

    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower(): 

            self.score = self.score + 1 
            
            print(f'Good Job, thats correct! Score: {self.score} / {self.question_number}')

        else: 
        
            print(f'Good try, the correct answer is: {correct_answer}. Score: {self.score} / {self.question_number}')

        print('\n')
