# -*- coding: utf-8 -*-
"""
Lesson 17 : 利用递归算法，生成分形图形（正方形地毯）
"""

import turtle

# 引入函数，过程，将重复动作组合在一个函数中。
def sierpinski2(turtle,length,level):
    if level == 0:
        square(turtle,length)
        
    else:
        #for i in range(3):重复三次画三角形，分别在三个顶点上画三角形
        curpos = t.position()  # 保留起始点坐标
        length /= 3.0
        sierpinski2(turtle,length,level-1)

        for _ in range(2):
            turtle.penup()
            turtle.forward(length)
            turtle.pendown()
            sierpinski2(turtle,length,level-1)
        
        for _ in range(2):
            turtle.penup()
            turtle.left(90)
            turtle.forward(length)
            turtle.right(90)  # 注意调整方向
            turtle.pendown()
            sierpinski2(turtle,length,level-1)

        turtle.penup()
        turtle.backward(2*length)
        turtle.pendown()
        sierpinski2(turtle,length,level-1)
        turtle.penup()
        turtle.forward(length)
        turtle.pendown()        
        sierpinski2(turtle,length,level-1)

        turtle.penup()
        turtle.backward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.pendown()
        sierpinski2(turtle,length,level-1)
            
        t.goto(curpos[0],curpos[1])  # 回到起始点，方向也复原
      
def square(turtle,length):
    for _ in range(4):
        turtle.forward(length)
        turtle.left(90)
        
    
scr = turtle.Screen()
t = turtle.Pen()    # 初始化乌龟程序，调出图形框，准备好画笔
t.shape("classic")  # 改变画笔形状为一只乌龟，缺省是箭头arrow，
# 还可以为 'circle'-圆, 'square'-正方形, 'triangle'-三角形, 'classic'.  

scr.bgcolor("white")  # (0.1,0.51,0.3)   # red,green,blue 取值在0和1之间。1代表255,

t.pensize(1)     # 改变线宽度
t.color("green")  # 改变画笔颜色,还有green,blue,black,white,pink,...,或者(r,g,b)

t.speed(0)
t.penup()
t.setposition(-200,-100)
t.pendown()

sierpinski2(t,300,4)

t.hideturtle()  # 隐藏乌龟图形

scr.exitonclick()
