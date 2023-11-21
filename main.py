from turtle import Turtle
from random import choice, randint
import colorgram

colors = colorgram.extract('hirst.png', 30)
rgbs = []

for c in colors:
    rgbs.append((c.rgb.r, c.rgb.g, c.rgb.b))


tim = Turtle()
tim.shape('circle')
tim.penup()
y = -250
tim.setpos(-250, y)


def paint():
    for draw in range(0, 10):
        tim.fd(50)
        tim.dot(30, (rgbs[randint(0, len(rgbs) - 1)][0]/255.0, rgbs[randint(0, len(rgbs) - 1)][1]/255.0, rgbs[randint(0, len(rgbs) - 1)][2]/255.0))


for _ in range(0, 10):
    paint()
    y += 50
    tim.setpos(-250, y)
tim.hideturtle()
tim.screen.mainloop()
