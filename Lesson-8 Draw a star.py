# -*- coding: utf-8 -*-
"""
Lesson 7 : 顺时针画图
"""

import turtle

wn = turtle.Screen()
t = turtle.Pen()    # 初始化乌龟程序，调出图形框，准备好画笔
t.shape("turtle")   # 改变画笔形状为一只乌龟，缺省是箭头arrow，
# 还可以为 'circle'-圆, 'square'-正方形, 'triangle'-三角形, 'classic'.  

wn.bgcolor("red")    # lightgreen

t.pensize(3)          # 改变画笔线宽度
t.color("yellow")     # 改变画笔颜色,还有green,blue,black,white,pink,...,或者(r,g,b)


#t.speed(5)      # 0,或者1~10， 1最慢slowest，10最快fastest

for i in range(5):
    t.stamp()
    t.fd(210)
    t.rt(144)     # 五角星的内角为36°   = right(180-36)


wn.exitonclick()   # 鼠标点击 就退出来。
