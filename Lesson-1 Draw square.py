# -*- coding: utf-8 -*-
"""
Lesson 1 : Draw a square 第一课：画一个正方形
"""

import turtle  # 调用 乌龟turtle库


def Square(pen, length):
    for _ in range(4):  # 重复4次
        pen.fd(length)  # 简写向前走, forward(len)
        pen.left(90)  # 左转90度 left(90)

def Tpen(shape="turtle", drawcolor='red', fillcolor='blue', size=3):
    Yang = turtle.Pen()    # 初始化乌龟程序，调出图形框，准备好画笔，给画师命名
    Yang.shape(shape)   # 改变画笔形状为一只乌龟，缺省是箭头arrow，
    # 还可以为 'circle'-圆, 'square'-正方形, 'triangle'-三角形, 'classic'.  

    Yang.pensize(size)
    Yang.color(drawcolor)
    Yang.fillcolor(fillcolor)

    return Yang

if __name__ == '__main__':
    win = turtle.Screen()  # Create a graphics windows 创建绘画窗口
    win.bgcolor('black')

    tp = Tpen()
    tp.begin_fill()
    Square(tp, 200)

    tp.end_fill()
    # 其他简写 penup()→up(), pendown()→down(),right()→rt()
    win.exitonclick()
