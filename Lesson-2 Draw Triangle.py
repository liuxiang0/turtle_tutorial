# -*- coding: utf-8 -*-
"""
Lesson 2 : Draw a triangle 画一个等边三角形
"""

import turtle

win = turtle.Screen()  # Create a graphics windows 创建绘画窗口

t = turtle.Pen()     # 初始化乌龟程序，调出图形框，准备好画笔
t.shape("triangle")  # 改变画笔形状为triangle，缺省是箭头arrow，
# 还可以为 'circle'-圆, 'square'-正方形, 'triangle'-三角形, 'classic'.  

t.width(5)          # 改变线宽度
t.color("red")      # 改变画笔颜色, 还有green,blue,black,white,pink,...,或者(r,g,b)

for i in range(3):  # 重复三次
    t.fd(200)  # 向前走200
    t.lt(120)  # 逆时针旋转120度，左转120°

win.exitonclick()