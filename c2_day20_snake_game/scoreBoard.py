from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "normal")
MOVE = False
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.write(f"SCORE: {self.score}", MOVE, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", MOVE, ALIGNMENT, FONT)
        # self.write(f"GAME OVER\nYour Score is {self.score}", MOVE, ALIGNMENT, FONT)

    def inc_score(self):
        self.score += 1
        self.clear()
        self.updateScoreBoard()


