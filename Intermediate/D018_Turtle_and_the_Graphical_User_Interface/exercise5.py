import turtle as t
import random

screen = t.Screen()
t.colormode(255)

def cc():
    return random.randint(0, 255)

timmy = t.Turtle()
timmy.speed(0)

for Spirograph in range(0, 72):
    timmy.color(cc(), cc(), cc())
    timmy.circle(100)
    timmy.right(5)

screen.exitonclick()
