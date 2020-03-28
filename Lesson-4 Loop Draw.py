# -*- coding: utf-8 -*-
"""
Lesson 4 : Draw a segment loop （循环画线段），就两个动作：平移与旋转
"""


import turtle


win = turtle.Screen()  # Create a graphics windows 创建绘画窗口

t = turtle.Pen()    # 初始化乌龟程序，调出图形框，准备好画笔
t.shape("turtle")   # 改变画笔形状为一只乌龟，缺省是箭头arrow，
# 还可以为 'circle'-圆, 'square'-正方形, 'triangle'-三角形, 'classic'.  

t.width(1)          # 改变线宽度
t.color("blue")     # 改变画笔颜色,还有green,blue,black,white,pink,...,或者(r,g,b)

# 利用中文命令来画图
前=t.forward
左=t.left

for i in range(1,37):  # 循环次数可以更改
    前(300)
    左(175)  # 逆时针旋转角度175°，也可以改变
    
win.exitonclick()