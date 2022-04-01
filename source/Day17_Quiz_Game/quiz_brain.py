from site import check_enableusersite


class QuizBrain:
    def __init__(self, questions_list = []):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_quesitons(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        curr_q =  self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q {self.question_number}: {curr_q.text} True or False ? ').lower()
        self.check_answer(user_answer, curr_q.answer)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print('Correct answer!')
            self.score += 1
        else:
            print('Wrong answer!')
        
        print(f'The correct answer is: {correct_answer}')
        print(f'Your current score is {self.score} / {self.question_number}\n')
