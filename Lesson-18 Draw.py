# -*- coding: utf-8 -*-
"""
Lesson 18 : 循环画折线，绕圆周一圈。
"""

import turtle 

powell = turtle.Turtle()
picture = turtle.Screen()

powell.speed(0)

for i in range(120):
    powell.forward(100)
    powell.right(30)
    powell.forward(20)
    powell.left(60)
    powell.forward(50)
    powell.right(30)
    
    powell.penup()
    powell.setposition(0, 0)
    powell.pendown()
    
    powell.right(3)
    
# turtle.done()
picture.exitonclick()      # 不能同时使用 turtle.done() 和 screen.exitonclick()
