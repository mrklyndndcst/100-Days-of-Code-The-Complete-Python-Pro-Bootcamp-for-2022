# import colorgram
#
# color_ink = []
# colors = colorgram.extract('image.jpg', 31)
#
# for ink in colors:
#     color_ink.append((ink.rgb[0], ink.rgb[1], ink.rgb[2]))
#
# print(color_ink)

color_list = [(28, 85, 140), (133, 74, 97), (189, 145, 169), (149, 91, 48), (12, 66, 129), (137, 156, 186),
              (185, 170, 31), (192, 158, 105), (213, 222, 233), (181, 96, 127), (14, 55, 97), (239, 223, 233),
              (133, 28, 48), (220, 172, 199), (241, 248, 246), (108, 119, 164), (231, 206, 7), (70, 28, 45),
              (74, 110, 89), (227, 205, 71), (76, 40, 22), (182, 103, 87), (116, 38, 30), (180, 183, 219),
              (141, 168, 148), (12, 81, 107), (92, 79, 17), (103, 144, 113), (36, 82, 63), (35, 60, 49)]

import turtle as t
import random

screen = t.Screen()
t.colormode(255)


def cc():
    return random.choice(color_list)


timmy = t.Turtle()
timmy.shape('circle')
timmy.speed(0)
timmy.penup()

x = -375
y = -375
number_in_x = 0

for Spirograph in range(100):
    timmy.color(random.choice(color_list))
    timmy.goto(x, y)
    timmy.position()
    timmy.dot(30)
    x += 75
    number_in_x += 1
    if number_in_x == 10:
        x = -375
        y += 75
        number_in_x = 0

screen.exitonclick()
