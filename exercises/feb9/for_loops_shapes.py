#Author: Avery Cordle

import turtle

turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(.5)
pen.color("black")

#ask the user for which shape they want
shapeS = turtle.textinput("Shapes", "Enter a square, a triangle, or a star: " ).lower().strip()
size = 100

pen.penup()
pen.setpos(-size/2, -size/2)
pen.pendown()

if shapeS == "square":
    #square
    for i in range(4):
        pen.forward(size)
        pen.left(90)
elif shapeS == "triangle":
    #triangle
    for i in range(3):
        pen.forward(size)
        pen.left(120)
elif shapeS == "star":
    for i in range(3):
        pen.forward(size)
        pen.left(120)
    pen.penup()
    pen.setpos(-size/2, -size/2 +size/2)
    pen.pendown()
    for i in range(3):
        pen.forward(size)
        pen.left(-120)




turtle.done()