# -*- coding: utf-8 -*-
"""
Lesson 9 : 循环画四边形
"""
import turtle
import random

mt = turtle.Turtle()

mt.hideturtle()
mt.speed(20)

scr = turtle.Screen()

mt.color("red")

for i in range(1,250):
   # mt.color(random.random(),random.random(),random.random())  # 随机颜色
    mt.forward(i*2)
    mt.right(98)
    
scr.exitonclick()
scr.exitonclick()