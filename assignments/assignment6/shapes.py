#Author: Avery Cordle

import turtle

turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(0)
pen.hideturtle()

#variables and list
shapeList = []
numShapes = int(turtle.numinput("Shapes", "Enter how many shapes you would like to draw: ", 10, 0, 100))
shapeSize = 100/numShapes
diameterPadding = turtle.window_width()/numShapes

#enter what shapes you want and append them
for i in range(numShapes):
    userShape = turtle.textinput("Shapes","Enter shape (circle, square, triangle, star, or diamond): ").lower().strip()
    shapeList.append(userShape)

#draw the shapes from the list

x = -turtle.window_width()/2 + diameterPadding/numShapes

for shape in shapeList:
    pen.penup()
    pen.setpos(x,0)
    pen.pendown()
    
    if shape == "circle":
        pen.circle(shapeSize/2)
    elif shape == "square":
        for i in range(4):
            pen.forward(shapeSize)
            pen.left(90)
    elif shape == "triangle": 
        for i in range(3):
            pen.forward(shapeSize)
            pen.left(120)
    elif shape == "star":
        for i in range(3):
            pen.forward(shapeSize)
            pen.left(120)
        pen.penup()
        pen.setpos(x,0+shapeSize/2)
        pen.pendown()
        for i in range(3):
            pen.forward(shapeSize)
            pen.left(-120)
    else:
        pen.setheading(45)
        for i in range(4):
            pen.forward(shapeSize/2)
            pen.left(90)
        pen.setheading(0)
    x +=diameterPadding

turtle.done()