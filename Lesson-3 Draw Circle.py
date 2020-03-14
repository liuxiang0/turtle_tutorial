# -*- coding: utf-8 -*-
"""
Lesson 3 : Draw a circle 画圆、半圆、弧、正多边形
"""

import turtle
from turtle_conf import Tpen


def Circles(pen, radius, num):
    for i in range(num):
        pen.circle(radius * (i + 1))

"""call: circle(radius)                  # 画整个圆， 负值也可以
    |--or: circle(radius, extent)        # 画弧--部分圆 180 半圆
    |--or: circle(radius, extent, steps)
    |--or: circle(radius, steps=6)       # 画六边形
"""        

win = turtle.Screen()  # Create a graphics windows 创建绘画窗口

t = Tpen(shape="turtle", drawcolor='red', size=2)

mycolor = ["red","green","blue"]

Circles(t, 30,5)
   
for i in range(3):
    t.color(mycolor[i])
    t.circle(-50*(i+1),steps=(i+1)*3)  # 画正n边形

t.reset()  # 清屏，重来

for i in range(3):
    t.color(mycolor[i])
    t.circle(50*(i+1),180)  # 画半圆

t.setposition(0,0)  # setpos(x,y) 移动圆点（0,0）
for i in range(3):
    t.color(mycolor[i])
    t.circle(-50*(i+1),180,(i+1)*4)  # 画正n边形 代表 半圆

win.exitonclick()