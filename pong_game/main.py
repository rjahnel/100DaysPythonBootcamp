from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

RIGHT_POS = (350, 0)
LEFT_POS = (-350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG-GAME")
screen.tracer(0)

l_paddle = Paddle(LEFT_POS)
r_paddle = Paddle(RIGHT_POS)
ball = Ball()
scoreboard = Scoreboard()
scoreboard.write_score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Right Paddle or Paddle left missed
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.add_score_l()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.add_score_r()

    if scoreboard.score_l == 5 or scoreboard.score_r == 5:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
