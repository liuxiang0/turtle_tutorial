# -*- coding: utf-8 -*-
"""
Lesson 2 : Draw a triangle 画一个等边三角形
"""

import turtle

from turtle_conf import Tpen

def Triangle(pen, length):
    for _ in range(3):  # 重复三次
        pen.fd(length)  # 向前走200
        pen.lt(120)  # 逆时针旋转120度，左转120°
        

if __name__=='__main__':
    win = turtle.Screen()  # Create a graphics windows 创建绘画窗口

    tp = Tpen(shape="triangle", size=3, drawcolor="red")  # 初始化乌龟程序，调出图形框，准备好画笔
    
    Triangle(tp, 300)

    win.exitonclick()