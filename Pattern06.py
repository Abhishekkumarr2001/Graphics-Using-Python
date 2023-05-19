import turtle as t
from turtle import *
colors = ["blue", "green", "purple", "cyan", "magenta", "violet"]
t.bgcolor('black')
t.reset()
t.tracer(0, 0)
for i in range(45):
    t.color(colors[i % 6])
    t.pendown()
    t.fd(2 + i * 5)
    t.left(45)
    t.width(i)
    t.penup()
    
t.update()
exitonclick()