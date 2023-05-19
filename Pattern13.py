from turtle import *

bgcolor("black")
speed(0)
hideturtle()
goto(60, 150)

for i in range(200):
    color("red")
    circle(i)
    color("orange")
    circle(i*0.8)
    right(3)
    forward(3)

done()
