# https://cs111.wellesley.edu/labs/lab02/colors
# https://www.rollingstone.com/culture/culture-news/steve-jobs-in-1994-the-rolling-stone-interview-231132/

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)

timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
my_screen.exitonclick()
