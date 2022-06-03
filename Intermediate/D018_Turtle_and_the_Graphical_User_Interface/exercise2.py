import turtle as t

tim = t.Turtle()
tim.color("red")

space = 10

for dashed_line in range(20):
    t.pd()
    t.forward(space)
    t.pu()
    t.forward(space)

screen = t.Screen()
screen.exitonclick()

