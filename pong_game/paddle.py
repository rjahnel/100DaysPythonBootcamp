from turtle import Turtle

MOVE_FACTOR = 20
STRETCH_FACTOR = (5, 1)
COLOR = "lawngreen"


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color(COLOR)
        self.shapesize(stretch_wid=STRETCH_FACTOR[0], stretch_len=STRETCH_FACTOR[1])
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + MOVE_FACTOR
        self.goto(self.xcor(), new_y, )

    def go_down(self):
        new_y = self.ycor() - MOVE_FACTOR
        self.goto(self.xcor(), new_y, )
