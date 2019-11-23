# -*- coding: utf-8 -*-
"""
Lesson 5 : Draw Star Delay 带延迟画图,五角星
"""

import turtle

wn = turtle.Screen()
t = turtle.Pen()    # 初始化乌龟程序，调出图形框，准备好画笔
t.shape("arrow")   # 改变画笔形状为一只乌龟，缺省是箭头arrow，
# 还可以为 'circle'-圆, 'square'-正方形, 'triangle'-三角形, 'classic'.  

wn.bgcolor("red")    # lightgreen

t.pensize(3)          # 改变画笔线宽度
t.color("yellow")     # 改变画笔颜色,还有green,blue,black,white,pink,...,或者(r,g,b)

wn.delay(10)     # 延迟100毫秒

for i in range(5):
    t.fd(300)
    t.rt(144)     # 五角星的内角为36°，也可以是left(144)

# t.fd(100)
# t.width(1)
"""
t.color("blue")

for i in range(5):
    t.fd(185.2)   # 黄金分割点， 300*0.618，or 300*（1-0.618）
    t.lt(144)     # 五角星的内角为36°
"""
wn.exitonclick()   # 鼠标点击 就退出来。
