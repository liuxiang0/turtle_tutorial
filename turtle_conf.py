'''turtle_color.py - get random pen color
'''

import random
import turtle

colors = ['red', 'green', 'blue', 'yellow', 'black', 'pink', 'cyan', 'purple', 'white']

t_color = random.choice(colors)

def random_color():
    # Get random color (r,g,b)

    r = random.randint(0,225)
    g = random.randint(0,225)
    b = random.randint(0,255)
    return (r,g,b)

def Tpen(shape="turtle", drawcolor='red', fillcolor='blue', size=3):
    Yang = turtle.Pen()    # 初始化乌龟程序，调出图形框，准备好画笔，给画师命名
    Yang.shape(shape)   # 改变画笔形状为一只乌龟，缺省是箭头arrow，
    # 还可以为 'circle'-圆, 'square'-正方形, 'triangle'-三角形, 'classic'.  

    Yang.pensize(size)  # equal to turtle.width(width=None)
    Yang.color(drawcolor)
    Yang.fillcolor(fillcolor)

    return Yang
