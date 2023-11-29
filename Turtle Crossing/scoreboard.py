from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=-280, y=260)
        self.write(f"Level : {self.score}", font=FONT,)

    def score_up(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(x=0, y=-260)
        self.write("Nice Try Noobies", align="center", font=('Google Sans',10, 'bold'))
