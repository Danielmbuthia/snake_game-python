from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.score = 0
        with open('data.txt') as score:
            self.highest_score = int(score.read())
        self.penup()
        self.goto(0, 270)
        self.update_score_board()
        self.hideturtle()

    def update_score_board(self):
        self.clear()
        self.write(f"Score is {self.score} Highest score {self.highest_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            with open('data.txt', 'w') as score:
                self.highest_score = self.score
                score.write(str(self.score))
        self.score = 0
        self.update_score_board()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write("Game Over", False, align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.update_score_board()
