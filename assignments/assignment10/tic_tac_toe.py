#Author: Avery Cordle

import turtle


turtle.setup(525,525)
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(.5)


x=0
y=0
charSize = 70

def draw_grid():
    #vertical
    pen.penup()
    pen.setpos(x-turtle.window_width()/2+turtle.window_width()/3,y-turtle.window_height()/2)
    pen.setheading(90)
    pen.pendown()
    for i in range (2):
        pen.forward(turtle.window_height())
        pen.penup()
        pen.setpos(x-turtle.window_width()/2+turtle.window_width()/3*2,y-turtle.window_height()/2)
        pen.pendown()
    #horizontal
    pen.penup()
    pen.setpos(x-turtle.window_width()/2,y-turtle.window_height()/2+turtle.window_height()/3)
    pen.setheading(0)
    pen.down()
    for i in range (2):
        pen.forward(turtle.window_width())
        pen.penup()
        pen.setpos(x-turtle.window_width()/2,y-turtle.window_height()/2+turtle.window_height()/3*2)
        pen.pendown()

def draw_X(x,y):
    pen.penup()
    pen.setpos(x,y)
    pen.setheading(45)
    pen.pendown()
    for i in range(4):
        pen.forward(charSize/2)
        pen.left(180)
        pen.forward(charSize/2)
        pen.left(90)

def draw_O(x,y):
    pen.penup()
    pen.setpos(x,y)
    pen.pendown()
    pen.circle(charSize/2)

clicks = 0

def draw_x_or_o(x,y):
    if clicks == 0:
        draw_X(x,y)
    elif clicks == 1:
        draw_O(x,y)

        

turtle.onscreenclick(draw_x_or_o)
if clicks == 0:
    clicks = 1
elif clicks == 1:
    clicks = 0
        








draw_grid()










turtle.done()