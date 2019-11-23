# -*- coding: utf-8 -*-
"""
Lesson 12 : 循环画圆
"""

import turtle

scr = turtle.Screen()
t = turtle.Pen()    # 初始化乌龟程序，调出图形框，准备好画笔
t.shape("turtle")   # 改变画笔形状为一只乌龟，缺省是箭头arrow，
# 还可以为 'circle'-圆, 'square'-正方形, 'triangle'-三角形, 'classic'.  

scr.bgcolor("white")   # (0.1,0.51,0.3)   # red,green,blue 取值在0和1之间。1代表255,

t.pensize(1)          # 改变线宽度
t.color("black")      # 改变画笔颜色,还有green,blue,black,white,pink,...,或者(r,g,b)

t.speed(0)

for n in range(50):
    t.circle(n*3)
    t.lt(16.5)             # 改变角度试试，5,10,16.5,30
        
scr.exitonclick()