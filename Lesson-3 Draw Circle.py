# -*- coding: utf-8 -*-
"""
Lesson 3 : Draw a circle 画圆、半圆、弧、正多边形
"""

import turtle

win = turtle.Screen()  # Create a graphics windows 创建绘画窗口

t = turtle.Pen()    # 初始化乌龟程序，调出图形框，准备好画笔
t.shape("turtle")   # 改变画笔形状为一只乌龟，缺省是箭头arrow，
# 还可以为 'circle'-圆, 'square'-正方形, 'triangle'-三角形, 'classic'.  

t.width(5)          # 改变线宽度
t.color("red")      # 改变画笔颜色,还有green,blue,black,white,pink,...,或者(r,g,b)
mycolor = ["red","green","blue"]

for i in range(3):
    t.color(mycolor[i])
    t.circle(50*(i+1))
    

"""call: circle(radius)                  # 画整个圆
    |--or: circle(radius, extent)        # 画弧--部分圆
    |--or: circle(radius, extent, steps)
    |--or: circle(radius, steps=6)       # 画六边形
"""
    
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