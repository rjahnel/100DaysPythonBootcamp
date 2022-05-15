from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.pencolor("blue")
        self.hideturtle()
        self.goto(x=-40, y=270)
        self.write_level()

    def add_level(self):
        self.level += 1
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"LEVEL : {self.level}", font=FONT)

    def game_over(self):
        self.goto(x=-50, y=0)
        self.write("GAME OVER", font=FONT)