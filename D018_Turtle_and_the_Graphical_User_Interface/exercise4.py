import turtle as t
import random

screen = t.Screen()
t.colormode(255)

def cc():
    return random.randint(0, 255)

timmy = t.Turtle()
timmy.pensize(10)
timmy.speed(0)

run = True
while run:
    timmy.forward(50)
    timmy.left(random.choice([0, 90, 180, 270]))
    timmy.color(cc(), cc(), cc())

screen.exitonclick()
