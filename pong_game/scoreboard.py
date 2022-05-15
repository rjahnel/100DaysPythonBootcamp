from turtle import Turtle

FONT = ('Courier', 30, 'normal')
COLOR = "yellow"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.pencolor(COLOR)
        self.hideturtle()
        self.goto(x=-50, y=260)
        self.write_score()

    def add_score_r(self):
        self.score_r += 1
        self.write_score()

    def add_score_l(self):
        self.score_l += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"{self.score_l} : {self.score_r}", font=FONT)

    def game_over(self):
        self.goto(x=-140, y=0)
        self.write("G A M E  O V E R", font=FONT)