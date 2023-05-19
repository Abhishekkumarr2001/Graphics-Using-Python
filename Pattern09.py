import turtle as t
from turtle import *

t.reset()
t.tracer(0, 0)

def ks(length, d):
    if d == 0:
        t.forward(length)
    else:
        length = length / 3
        d = d - 1
        ks(length, d)
        t.right(60)
        ks(length, d)
        t.left(120)
        ks(length, d)
        t.right(60)
        ks(length, d)


colors = ["red", "orange", "pink"]
for i in range(3):
    t.color(colors[i])
    ks(200, 3)
    t.left(120)

t.update()
exitonclick()