#author: Avery Cordle

import turtle
import random

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

def getColors():
    colors = []
    try:
        with open ("scene.txt") as file:
            for line in file:
                sceneColor = line.replace("\n","")
                colors.append(sceneColor)
    except FileNotFoundError:
        print("Sorry, invalid file")
    return colors

def drawColorStrip(y,height,color):
    pen.penup()
    pen.setpos(-turtle.window_width()/2,y)
    pen.fillcolor(color)
    pen.color(color)
    pen.pendown()
    pen.begin_fill()
    for i in range(4):
        if i %2 ==0:
            pen.forward(turtle.window_width())
        else:
            pen.forward(height)
        pen.left(90)
    pen.end_fill()

colorList = getColors()
height = int(turtle.window_height()/len(colorList))
y = -int(turtle.window_height()/2)

for color in colorList:
    drawColorStrip(y,height,color)
    y+=height

turtle.done()