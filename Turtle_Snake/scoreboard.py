from turtle import Turtle
from food import Food

with open("highscore.txt") as file:
    x = file.read()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.highscore = int(x);
        self.goto(0, 350)
        self.keep_score()

    def keep_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.keep_score()

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as sco:
                sco.write(str(self.highscore))
        self.score = 0
        self.keep_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game over", align="center", font=("Courier", 24, "normal"))
