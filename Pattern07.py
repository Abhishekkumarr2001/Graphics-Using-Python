import turtle as t
from turtle import *

t.reset()
t.bgcolor('black')
t.color("red")
t.speed(0)
for angle in range(0, 360, 15):
    t.seth(angle)
    t.circle(100)

exitonclick()
