from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.update_score_board()
        self.hideturtle()

    def update_score_board(self):
        self.write(f"Score is {self.score} ", False, align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()
