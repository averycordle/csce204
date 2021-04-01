#Author: Avery Cordle
import turtle
import random

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

def getScene():
    sceneShapes = []
    with open ("assignments/assignment11/scene.txt") as file:
        for line in file:
            shape = line.replace("\n","")
            sceneShapes.append(shape)
        return sceneShapes

def drawStar(x,width):
    drawTriangle(x,y,size)
    drawUpsideDownTriangle(x,y,size)

def drawTree(x,width):
    drawTriangle(x,y,size)
    drawTriangle(x+size/12,y+size*.3,size*.85)
    drawTriangle(x+size/7,y+size*.55,size*.75)

def drawTriangle(x,y,size):
    pen.penup()
    pen.setpos(-turtle.window_width()/2+x, y)
    pen.pendown()
    pen.begin_fill()
    for i in range(3):
        pen.forward(size)
        pen.left(120)
    pen.end_fill()

def drawUpsideDownTriangle(x,y,size):
    pen.penup()
    pen.setpos(-turtle.window_width()/2+x, y+size/2)
    pen.pendown()
    pen.begin_fill()
    for i in range(3):
        pen.forward(size)
        pen.left(-120)
    pen.end_fill()

shapeList = getScene()
numShapes = len(shapeList)
padding = turtle.window_width()/numShapes/numShapes
width = turtle.window_width()/numShapes 
size = width/2
x = 0+padding
y = -width/2

for shape in shapeList:
    if shape == "star":
        pen.fillcolor("gold")
        pen.color("gold")
        drawStar(x,width)
    else:
        pen.fillcolor("green")
        pen.color("green")
        drawTree(x,width)
    x += width

turtle.done()