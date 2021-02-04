#Author: Avery Cordle
import turtle
#create shapes based off of user input
turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(.5)

#ask the user
shape = turtle.textinput("Shapes", "Enter Shape: ").lower().strip()
color = turtle.textinput("Colors", "Enter Favorite Color: ").lower().strip()
shapeSize = turtle.numinput("Shape Size", "Size (1-10)", 5,1,10)*45

if shape == "circle":
    pen.penup()
    pen.setpos(0,-shapeSize/2)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(shapeSize/2)
    pen.end_fill()
elif shape == "square":
    pen.penup()
    pen.setpos(-shapeSize/2,-shapeSize/2)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.setheading(360)
    for i in range(4):
        pen.forward(shapeSize)
        pen.left(90)
    pen.end_fill()
elif shape == "triangle":
    pen.penup()
    pen.setpos(-shapeSize/2,-shapeSize/2)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.setheading(360)
    for i in range(3):
        pen.forward(shapeSize)
        pen.left(120)
    pen.end_fill()



turtle.done()