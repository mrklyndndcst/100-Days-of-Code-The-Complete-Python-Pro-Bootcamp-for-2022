class QuizBrain:
    def __init__(self, question_list):
        score = 0
        question_number = 0

        while question_number != len(question_list):
            player_answer = input(f"Q.{question_number + 1}: {question_list[question_number].text} (True/False)?: ")
            if player_answer.lower() == question_list[question_number].answer.lower():
                score += 1
                print("You got it right!")
            else:
                print("You got it wrong!")
            print(f"The correct answer was: {question_list[question_number].answer}.")
            print(f"Your current score is: {score}/{question_number + 1}")
            question_number += 1
            print('\n')
        print("You've completed the quiz")
        print(f"Your final score was : {score}/{question_number}")
