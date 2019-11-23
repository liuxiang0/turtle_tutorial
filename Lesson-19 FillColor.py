# -*- coding: utf-8 -*-
"""
Lesson 19 : 填充颜色
"""

import turtle 

powell = turtle.Turtle()
picture = turtle.Screen()

powell.speed(5)
powell.color("red","yellow")
powell.begin_fill()

#for i in range(120):
while True:
    powell.forward(200)
    powell.left(170)
    if abs(powell.pos()) < 1:    # turtle.pos() 返回的值是turtle.Vec2D,重新回到了起始点
        break
  
powell.end_fill()
# turtle.done()
picture.exitonclick()      # 不能同时使用 turtle.done() 和 screen.exitonclick()
