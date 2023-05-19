import turtle
import random

window=turtle.Screen()
t=turtle.Turtle()
window.colormode(225)
t.speed(0)
t.width(1)
window.bgcolor("black")
t.pencolor("yellow")

def shape(angle, side, limit):
    reverseDirection=200
    t.forward(side)

    if side%(reverseDirection*2)==0:
        angle=angle+2
        print(side)

    elif side%(reverseDirection)==0:
        angle=angle-2
        print(side)
    
    t.right(angle)
    side=side+2

    if side<limit:
        shape(angle,side,limit)


shape(119, 0 ,600)
window.exitonclick()