# -*- coding: utf-8 -*-
"""
Lesson 16 : 迭代生成多边形和螺线
"""

import turtle

# 引入函数，过程，将重复动作组合在一个函数中。
def draw_triangle(turtle,length):
    for i in range(3):
        turtle.fd(length)
        turtle.left(120)

def draw_poly(turtle,length,n):     # draw n-polygon 画正n边形
    for i in range(n):
        turtle.fd(length)
        turtle.left(360/n)    

def draw_spiral(turtle,length,angle,scale,n):
    for i in range(1,n):
        turtle.forward(length)
        turtle.left(angle)
        length *= scale
    
scr = turtle.Screen()
t = turtle.Pen()    # 初始化乌龟程序，调出图形框，准备好画笔
t.shape("triangle")   # 改变画笔形状为一只乌龟，缺省是箭头arrow，
# 还可以为 'circle'-圆, 'square'-正方形, 'triangle'-三角形, 'classic'.  

scr.bgcolor("white")   # (0.1,0.51,0.3)   # red,green,blue 取值在0和1之间。1代表255,

t.pensize(1)          # 改变线宽度
t.color("green")      # 改变画笔颜色,还有green,blue,black,white,pink,...,或者(r,g,b)

t.speed(0)

draw_spiral(t,10,90,1.05,60)

"""for n in range(1,50):
    t.fd(n)                 # 也可以隐藏之，原地旋转。
    draw_poly(t,n,4)        # 改变 为正 5,4,3边形
    t.right(60)             # 改变角度试试，5,10,15
   """     
scr.exitonclick()
