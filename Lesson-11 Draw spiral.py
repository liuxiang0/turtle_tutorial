# -*- coding: utf-8 -*-
"""
Lesson 11 : 画类似螺线的正n边形
"""

import turtle

scr = turtle.Screen()
t = turtle.Pen()    # 初始化乌龟程序，调出图形框，准备好画笔
t.shape("turtle")   # 改变画笔形状为一只乌龟，缺省是箭头arrow，
# 还可以为 'circle'-圆, 'square'-正方形, 'triangle'-三角形, 'classic'.  

scr.bgcolor("white")   # (0.1,0.51,0.3)   # red,green,blue 取值在0和1之间。1代表255,

t.pensize(2)          # 改变线宽度
t.color("black")      # 改变画笔颜色,还有green,blue,black,white,pink,...,或者(r,g,b)

for n in range(30):
    t.fd(n*10)
    t.lt(72)             # 改变角度试试，90,120，72，...
        
scr.exitonclick()