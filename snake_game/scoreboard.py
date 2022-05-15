from turtle import Turtle

FONT = ('Courier', 18, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.hideturtle()
        self.goto(x=-40, y=280)
        self.write_score()

    def add_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score : {self.score}", font=FONT)

    def game_over(self):
        self.goto(x=-50, y=0)
        self.write("GAME OVER", font=FONT)