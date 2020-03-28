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
colors = ['red', 'green', 'blue', 'yellow', 'pink', 'cyan', 'purple', 'white']
#'black',
myShape = random.choice(shapes)
myColor = random.choice(colors)
step = random.randrange(50, 200, 5)

win = turtle.Screen()  # Create a graphics windows 创建绘画窗口

pen = turtle.Pen()    # 初始化乌龟程序，调出图形框，准备好画笔，给画师命名
pen.shape(myShape)   # 改变画笔形状为一只乌龟，缺省是箭头arrow，
# 还可以为 'circle'-圆, 'square'-正方形, 'triangle'-三角形, 'classic'.  
pen.color(myColor)
turtle.bgcolor("black")

def random_color():
    # Get random color (r,g,b)

    r = random.randint(0,225)
    g = random.randint(0,225)
    b = random.randint(0,255)
    return (r,g,b)

def Square(length=100, sides=4):
    ''' Square(): 边长 length '''
    RegularPolygon(length,4)

def Triangle(length=100):
    ''' Triangle(): 边长 length '''
    RegularPolygon(length,3)

def Pentagon(length=100):
    ''' Pentagon(): 边长 length '''
    RegularPolygon(length,5)

def Hexagon(length=100):
    ''' Hexagon(): 边长 length '''
    RegularPolygon(length,6)

def Heptagon(length=100):
    ''' Heptagon(): 边长 length '''
    RegularPolygon(length,7)

def Octagon(length=100):
    ''' Heptagon(): 边长 length '''
    RegularPolygon(length,8)

def RegularPolygon(length=100, sides=5):
    ''' RegularPolygon(): 边长 length，边数 sides '''
    angle = 360 / sides
    for _ in range(sides):  # 重复次数
        pen.fd(length)  # 向前走
        pen.lt(angle)  # 逆时针旋转角度

def Spirals(colors, delta):
    '''Spirals(sides): sides 边数，对应colors个数 '''
    sides = len(colors)
    pen.speed(0)  # fastest speed of drawing 0
    for x in range(1,360,1):
        pen.pencolor(colors[x % sides])  #random.choice(colors))
        pen.width(x/100 + 1)
        pen.forward(x)
        pen.left(360 / sides - delta)  # 错位角度=0，就是正蜘蛛网，

def Spiral(angle=24):

    pen.speed(0)
    for size in range(1, 173, 2):  # start with size = 5 and grow by 2
        #pen.stamp()        # leave an impression on the canvas
        pen.dot()
        pen.forward(size)  # move turtle along
        pen.right(angle)      # and turn her


def Spiral4():
    turtle.colormode(255)  # this is something that is irrelevant at this point
                    # check the pthondocs link
    pen.speed(0)
    for x in range(1,400):
        r = random.randint(0,255)  # makes variables r,g,b whose value is an integer
        g = random.randint(0,255)  # which is between 0 and 255. It is random and
        b = random.randint(0,255)  # changes every time the loop runs
        pen.pencolor(r,g,b)  # changes the color of the pen to the rgb coordinates
        pen.forward(50+x)
        pen.right(90.911)

def Spiral3():
    turtle.colormode(255)  # this is something that is irrelevant at this point
                    # check the pthondocs link
    pen.speed(0)
    for x in range(1,400):
        r = random.randint(0,255)  # makes variables r,g,b whose value is an integer
        g = random.randint(0,255)  # which is between 0 and 255. It is random and
        b = random.randint(0,255)  # changes every time the loop runs
        pen.pencolor(r,g,b)  # changes the color of the pen to the rgb coordinates
        pen.forward(50+x)
        pen.right(120.911)

def space():
    pen.penup()
    pen.forward(100)
    pen.pendown()

def a():
    for _ in range(450): #this is an A
        pen.forward(2)
        pen.left(1)
    pen.forward(140)
    pen.right(180)
    pen.forward(240)
    for _ in range(90):
        pen.forward(1)
        pen.left(1)
    pen.penup()
    pen.forward(100)
    pen.left(90)
    pen.forward(25)
    pen.right(90)
    pen.pendown()

def b():
    pen.left(90)
    pen.forward(300)
    pen.backward(250)
    for _ in range(180):
        pen.forward(3)
        pen.right(2)
    pen.backward(100)
    pen.penup()
    pen.right(90)
    pen.forward(300)
    pen.pendown()

def c():
    pen.penup()
    pen.forward(100)
    pen.left(90)
    pen.forward(50)
    pen.right(90)
    pen.pendown()
    pen.right(135)
    for _ in range(275):
        pen.forward(2)
        pen.right(1)
    pen.penup()
    pen.right(45)
    pen.forward(200)
    pen.left(90)
    pen.forward(100)
    pen.pendown()


def drawABC():
    draw = {" ":space, "a":a, "b":b, "c":c}

    for letter in [' ', 'a','b', 'c']:
        if letter in draw.keys():
            draw[letter]()    

if __name__ == '__main__':
    win.title("Welcome to turtle graphics!")
    #Spirals(colors, 2)
    Spiral3()

    win.onkey(Triangle, "A")
    pen.color(random.choice(colors))
    win.onkey(Square, "B")
    pen.color(random.choice(colors))
    win.onkey(RegularPolygon, "C")

    pen.color(random.choice(colors))
    length = random.randint(100,200)
    sides = random.randint(3,23)
    #win.onkey(RegularPolygon(length, sides), "space")

    win.listen()
    #RegularPolygon()
    #win.exitonclick()
    #win.mainloop()
    #RegularPolygon(sides=7)

    # 其他简写 penup()→up(), pendown()→down(),right()→rt()
    win.exitonclick()
