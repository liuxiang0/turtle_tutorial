# -*- coding: utf-8 -*-
"""
Lesson 6 : 给定速度画螺线图
"""

import turtle


wn = turtle.Screen()
monkey = turtle.Pen()    # 初始化乌龟程序，调出图形框，准备好画笔
'''
monkey.shape("turtle")   # 改变画笔形状为一只乌龟，缺省是箭头arrow，
# 还可以为 'circle'-圆, 'square'-正方形, 'triangle'-三角形, 'classic'.  

wn.bgcolor("red")  # lightgreen
monkey.pensize(3)        # 改变画笔线宽度
monkey.color("yellow")   # 改变画笔颜色,还有green,blue,black,white,pink,...,或者(r,g,b)

#monkey.speed(5)  # 0,或者1~10， 1最慢slowest，10最快fastest
for i in range(5):
    monkey.speed(2*i)  # 画的速度变化
    monkey.stamp()  # 留痕迹
    monkey.fd(200)
    monkey.lt(144)  # 五角星的内角为36°
'''

wn.bgcolor('orange')
monkey.color("white")  # 改变画笔颜色
monkey.speed(7)
monkey.pensize(1)
# 画类似螺线或蜘蛛网
monkey.shape('triangle')
for size in range(5, 173, 2):  # start with size = 5 and grow by 2
    monkey.stamp()        # leave an impression on the canvas
    monkey.forward(size)  # move turtle along
    monkey.right(24)      # and turn her

wn.exitonclick()  # 鼠标点击就退出