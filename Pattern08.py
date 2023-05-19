import turtle as t
from turtle import *

def drawfib(n, len_ang):
    t.forward(2 * len_ang)
    if n == 0 or n == 1:
        pass
    else:
        t.left(len_ang)
        drawfib(n - 1, len_ang)
        t.right(2 * len_ang)
        drawfib(n - 2, len_ang)
        t.left(len_ang)
    t.backward(2 * len_ang)

start_points = [[-300, 250], [-150, 250],[-300, 110], [-80, 110],[-300, -150], [50, -150]]

# For each starting point, draw a tree with n varying
# between 1 and 6 and len_ang set to 30.
# n = 0
# for start_point in start_points:
#     x, y = start_point
#     n = n + 1
#     t.penup()
#     t.setpos(x, y)
#     t.pendown()
#     drawfib(n, 30)
t.reset()
t.tracer(0, 0)
drawfib(30, 15)
t.update()
t.tracer(1, 15)
exitonclick()