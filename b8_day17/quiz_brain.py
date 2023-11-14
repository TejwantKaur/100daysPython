class QuizBrain:
    def __init__(self, q_list):
        self.ques_num = 0;
        self.ques_list = q_list
        self.score = 0

    def next_question(self):
        curr_ques = self.ques_list[self.ques_num]
        self.ques_num += 1
        user_ans = input(f"Q{self.ques_num}. {curr_ques.text} (True/False): ")
        self.check_ans(user_ans, curr_ques.ans)

    def still_has_ques(self):
        return self.ques_num < len(self.ques_list)

    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("It's wrong!")

        print(f"The correct answer is : {correct_ans} ")
        print(f"Your current Score is {self.score}/{self.ques_num}")




