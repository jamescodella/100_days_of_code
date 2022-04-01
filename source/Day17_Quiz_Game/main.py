from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    question_bank.append(Question(q['question'], q['correct_answer']))

qb = QuizBrain(question_bank)

while qb.still_has_quesitons():
    result = qb.next_question()

print('You\'ve completed the quiz')
print(f'Your final score was {qb.score} / {len(qb.questions_list)} ')