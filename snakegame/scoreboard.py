from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highest_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} Highest Score : {self.highest_score} ", align="center", font=('Google Sans', 10, 'bold'))

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highest_score}")
        self.score = 0
        self.update_score()

    def score_up(self):
        self.score += 10
        self.clear()
        self.write(f"Score : {self.score} Highest Score : {self.highest_score} ", align="center", font=('Google Sans', 10, 'bold'))
