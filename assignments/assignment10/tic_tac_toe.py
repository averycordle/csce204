#Author: Avery Cordle

import turtle

turtle.setup(475,475)
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(.5)

x=0
y=0
charSize = 100
isX = True

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
    pen.setpos(getXCoord(x),getYCoord(y))
    pen.setheading(45)
    pen.pendown()
    for i in range(4):
        pen.forward(charSize/2)
        pen.left(180)
        pen.forward(charSize/2)
        pen.left(90)

def draw_O(x,y):
    pen.setheading(0)
    pen.penup()
    pen.setpos(getXCoord(x),getYCoord(y)-charSize/2)
    pen.pendown()
    pen.circle(charSize/2)

def draw_x_or_o(x,y):
   global isX
   if isX:
      draw_O(x,y)
      isX = False
   else:
      draw_X(x,y)
      isX = True
        
def getXCoord(x):
    if x>-turtle.window_width()/2 and x<=-turtle.window_width()/2+turtle.window_width()/3:
        x = -turtle.window_width()/2+turtle.window_width()/6
        return x
    elif x>-turtle.window_width()/2+turtle.window_width()/3 and x<=-turtle.window_width()/2+turtle.window_width()/3*2:
        x = 0
        return x
    elif x>-turtle.window_width()/2+turtle.window_width()/3*2 and x<=-turtle.window_width()/2+turtle.window_width()/3*3:
        x = turtle.window_width()/2-turtle.window_width()/6
        return x

def getYCoord(y):
    if y>-turtle.window_height()/2 and y<=-turtle.window_height()/2+turtle.window_height()/3:
        y = -turtle.window_height()/2+turtle.window_height()/6
        return y
    elif y>-turtle.window_height()/2+turtle.window_height()/3 and y<=-turtle.window_height()/2+turtle.window_height()/3*2:
        y = 0
        return y
    elif y>-turtle.window_height()/2+turtle.window_height()/3*2 and y<=-turtle.window_height()/2+turtle.window_height()/3*3:
        y = turtle.window_height()/2-turtle.window_height()/6
        return y

def draw_Play(x,y):
    draw_x_or_o(x,y)

turtle.onscreenclick(draw_Play)
draw_grid()

turtle.done()