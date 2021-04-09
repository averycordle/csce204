import turtle
import random

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

def getScene():
    sceneColors = []
    with open("programs/11-file-writing/scene.txt") as file:
        for line in file:
            sceneColor = line.replace("\n", "").strip().lower()
            sceneColors.append(sceneColor)
        return sceneColors

def drawColorStrip(y, height, color):
    #draw the bars
    pen.penup()
    pen.setpos(-turtle.window_width()/2,y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range (4):
        if i % 2 == 0:
            pen.forward(turtle.window_width())
        else: 
            pen.forward(height)
        pen.left(90)
    pen.end_fill()

def saveScene(colorList):
    with open("programs/11-file-writing/scene.txt", "w") as file:
        for sceneColor in colorList:
            file.write(sceneColor + "\n")

def changeColor(x,y):
    userColor = turtle.textinput("Colors", "Enter Color: ").strip()
    stripHeight = turtle.window_height()/len(colorList)
    section = int(y//stripHeight) #int it to get no decimal in division
    #now we do the work to update the file - it gets trippy
    index = -section + (len(colorList)-1)//2 #fucking crazy - one system starts at zero, the other systems starts zero in the middle
    colorList[index] = userColor
    saveScene(colorList)
    drawColorStrip(section*stripHeight, stripHeight,userColor)

colorList = getScene()
numColors = len(colorList)
height = turtle.window_height()/numColors
y = turtle.window_height()/2

for myColor in colorList:
    y -= height
    drawColorStrip(y,height,myColor)

turtle.onscreenclick(changeColor)

turtle.done()