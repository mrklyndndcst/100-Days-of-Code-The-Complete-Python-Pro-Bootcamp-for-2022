from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for add in question_data:
    question = add['question']
    answer = add['correct_answer']
    new_question = QuestionModel(question, answer)
    question_bank.append(new_question)

QuizBrain(question_bank)
