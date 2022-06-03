from turtle import *

timmy = Turtle()
timmy.color("red")

for square in range(4):
    timmy.forward(100)
    timmy.right(90)

screen = Screen()
screen.exitonclick()