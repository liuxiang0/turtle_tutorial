# -*- coding: utf-8 -*-
"""
Lesson 1 : Draw a square 第一课：画一个正方形
"""

import turtle  # 调用 乌龟turtle库

win = turtle.Screen()  # Create a graphics windows 创建绘画窗口

Yang = turtle.Pen()    # 初始化乌龟程序，调出图形框，准备好画笔，给画师命名
Yang.shape("turtle")   # 改变画笔形状为一只乌龟，缺省是箭头arrow，
# 还可以为 'circle'-圆, 'square'-正方形, 'triangle'-三角形, 'classic'.  

for i in range(4):  # 重复4次
    Yang.fd(100)  # 简写向前走100步 forward(100)
    Yang.lt(90)  # 左转90度 left(90)

# 其他简写 penup()→up(), pendown()→down(),right()→rt()
win.exitonclick()