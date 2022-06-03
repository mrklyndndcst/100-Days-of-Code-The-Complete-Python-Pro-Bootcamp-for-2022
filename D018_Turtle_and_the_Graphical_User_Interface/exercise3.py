import turtle as t
import random

screen = t.Screen()
t.colormode(255)

def cc():
    return random.randint(0, 255)

timmy = t.Turtle()
timmy.pencolor(cc(), cc(), cc())

angle = 360
x = 3
run = True

while run:
    timmy.forward(50)
    timmy.left(angle/x)
    if abs(timmy.pos()) < 1:
        x += 1
        timmy.pencolor(cc(), cc(), cc())
        timmy.color(cc(), cc(), cc())
    if x == 13:
        break

screen.exitonclick()
