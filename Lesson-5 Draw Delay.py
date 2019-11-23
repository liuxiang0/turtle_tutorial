# -*- coding: utf-8 -*-
"""
Lesson 5 : Draw Star Delay 以红色为背景，带延迟一笔画五角星(n=5)或n角♥
"""

import turtle


wn = turtle.Screen()
t = turtle.Pen()  # 初始化乌龟程序，调出图形框，准备好画笔
t.shape("arrow")  # 改变画笔形状为一只乌龟，缺省是箭头arrow，
# 还可以为 'circle'-圆, 'square'-正方形, 'triangle'-三角形, 'classic'.  

wn.bgcolor("red")  # lightgreen

t.pensize(3)       # 改变画笔线宽度
t.color("yellow")  # 改变画笔颜色,还有green,blue,black,white,pink,...,或者(r,g,b)

wn.delay(10)  # 延迟100毫秒

n = 7  # n为奇数
for _ in range(n):
    t.fd(307)  # prime 
    t.rt(180-180/n)  # 五角星的内角为36°=180°/5，也可以是left(144)

wn.exitonclick()  # 鼠标点击就退出来

'''
t.fd(100)
t.width(1)
t.color("blue")

for i in range(5):
    t.fd(185.2)   # 黄金分割点， 300*0.618，or 300*（1-0.618）
    t.lt(144)     # 五角星的内角为36°
'''