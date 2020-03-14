# -*- coding: utf-8 -*-
"""
Lesson 12 : 循环画圆
"""

import turtle
from turtle_conf import t_color, random_color, colors
import random


def draw_circles():
    t = turtle.Pen()    # 初始化乌龟程序，调出图形框，准备好画笔
    t.shape("circle")   # 改变画笔形状为一只乌龟，缺省是箭头arrow，
    # 还可以为 'circle'-圆, 'square'-正方形, 'triangle'-三角形, 'classic'.  
    t.pensize(3)          # 改变线宽度
    t.speed(0)
    turtle.colormode(255)  # 

    for n in range(30):
        #t.color(random.choice(colors))  # 改变画笔颜色,还有green,blue,black,white,pink,...,或者(r,g,b)
        r = random.randint(0,225)
        g = random.randint(0,225)
        b = random.randint(0,225)
        t.color(r,g,b)
        t.circle(n*3)
        t.lt(19)  # 改变角度试试，5,10,16.5,30

if __name__ == '__main__':
    scr = turtle.Screen()
    scr.bgcolor("white")   # (0.1,0.51,0.3)   # red,green,blue 取值在0和1之间。1代表255,
    draw_circles()
    scr.exitonclick()