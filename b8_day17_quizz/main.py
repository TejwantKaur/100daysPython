from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    ques = item["question"]
    ans = item["correct_answer"]
    new_ques = Question(ques, ans)
    question_bank.append(new_ques)

# print(question_bank)
# print(question_bank[1].ans)

quiz = QuizBrain(question_bank)

while quiz.still_has_ques():
    quiz.next_question()

print()
print("You have completed the quiz!")
print(f"Your final score is : {quiz.score}/{quiz.ques_num}")
