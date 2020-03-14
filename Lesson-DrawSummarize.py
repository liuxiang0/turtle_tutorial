# -*- coding: utf-8 -*-
"""
Summarize: Draw polygons

# Turtle motion
## Move and draw:
    forward() | fd()
    backward() | bk() | back()
    right() | rt()
    left() | lt()
    goto() | setpos() | setposition()
    setx()
    sety()
    setheading() | seth()
    home()
    circle()
    dot()
    stamp()
    clearstamp()
    clearstamps()
    undo()
    speed()

## Tell Turtle’s state
    position() | pos()
    towards()
    xcor()
    ycor()
    heading()
    distance()
## Setting and measurement
    degrees()
    radians()

# Pen control
## Drawing state
    pendown() | pd() | down()
    penup() | pu() | up()
    pensize() | width()
    pen()
    isdown()
    Color control
    color()
    pencolor()
    fillcolor()
    Filling
    filling()
    begin_fill()
    end_fill()
## More drawing control
    reset()
    clear()
    write()
"""

import turtle  # 调用 乌龟turtle库
import random

shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
colors = ['red', 'green', 'blue', 'yellow', 'black', 'pink', 'cyan', 'purple', 'white']

myShape = random.choice(shapes)
myColor = random.choice(colors)
step = random.randrange(50, 200, 5)

win = turtle.Screen()  # Create a graphics windows 创建绘画窗口

pen = turtle.Pen()    # 初始化乌龟程序，调出图形框，准备好画笔，给画师命名
pen.shape(myShape)   # 改变画笔形状为一只乌龟，缺省是箭头arrow，
# 还可以为 'circle'-圆, 'square'-正方形, 'triangle'-三角形, 'classic'.  
pen.color(myColor)

def random_color():
    # Get random color (r,g,b)

    r = random.randint(0,225)
    g = random.randint(0,225)
    b = random.randint(0,255)
    return (r,g,b)

def Square(length=100, sides=4):
    ''' Square(): 边长 length，转角 angle （度数 °），边数 sides
    '''
    angle = 360 / sides
    for _ in range(sides):  # 重复4次
        pen.fd(length)  # 简写向前走100步 forward(100)
        pen.lt(angle)  # 左转90度 left(90)

def Triangle(length=100, sides=3):
    ''' Triangle(): 边长 length，转角 angle （度数 °），边数 sides
    '''
    angle = 360 / sides
    for _ in range(sides):  # 重复三次
        pen.fd(length)  # 向前走200
        pen.lt(angle)  # 逆时针旋转120度，左转120°

def RegularPolygon(length=100, sides=5):
    ''' RegularPolygon(): 边长 length，转角 angle （度数 °），边数 sides
    '''
    angle = 360 / sides
    for _ in range(sides):  # 重复次数
        pen.fd(length)  # 向前走
        pen.lt(angle)  # 逆时针旋转角度


if __name__ == '__main__':
    win.title("Welcome to turtle graphics!")
    #Square()
    #Triangle()
    win.onkey(Triangle, "Up")

    pen.color(random.choice(colors))
    win.onkey(Square, "Down")

    pen.color(random.choice(colors))
    win.onkey(RegularPolygon, "Left")

    pen.color(random.choice(colors))
    length = random.randint(100,200)
    sides = random.randint(6,23)
    win.onkey(RegularPolygon(length, sides), "space")

    win.listen()
    #RegularPolygon()
    #win.exitonclick()
    #win.mainloop()
    #RegularPolygon(sides=7)

    # 其他简写 penup()→up(), pendown()→down(),right()→rt()
    win.exitonclick()
