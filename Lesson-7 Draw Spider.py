# -*- coding: utf-8 -*-
"""
Lesson 7 : 给定n值，画正n边形的轴
"""

import turtle


wn = turtle.Screen()
xpen = turtle.Turtle()
xpen.shape("triangle")

n = int(input("How many legs should this sprite have? "))
angle = 360 / n
len = 168

for _ in range(n):
    # draw the leg
    xpen.right(angle)
    xpen.forward(len)
    xpen.stamp()

    # go back to the middle and turn back around
    xpen.right(180)
    xpen.forward(len)
    xpen.right(180)

xpen.shape("circle")
wn.exitonclick()
