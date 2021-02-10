#Author: Avery Cordle

import turtle
turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(0.5)
pen.color("black")

houseSize = 100

#draw
#house
pen.penup()
pen.setpos(-houseSize/2, -houseSize/2)
pen.pendown()
pen.color("black")
pen.fillcolor("orange")
pen.begin_fill()
for i in range(4):
    pen.forward(houseSize)
    pen.left(90)
pen.end_fill()  

#roof
pen.penup()
pen.setpos(-houseSize/1.7, houseSize/2)
pen.pendown()
pen.fillcolor("purple")
pen.begin_fill()
for i in range(3):
    pen.forward(houseSize*1.2)
    pen.left(120)
pen.end_fill()    

#tree trunk
pen.penup()
pen.setpos(houseSize, -houseSize/2)
pen.pendown()
pen.color("brown")
pen.fillcolor("brown")
pen.begin_fill()
for i in range(4):
    pen.forward(houseSize/4)
    pen.left(90)
pen.end_fill()    

#tree top
pen.penup()
pen.setpos(houseSize*1.12, -houseSize/3)
pen.pendown()
pen.color("green")
pen.fillcolor("green")
pen.begin_fill()
pen.circle(houseSize/4)
pen.end_fill()  

#sun
pen.penup()
pen.setpos(-houseSize*1.5, houseSize*2)
pen.pendown()
pen.setheading(180)
pen.color("yellow")
for i in range(20):
    pen.forward(houseSize/2)
    pen.left(180)
    pen.forward(houseSize/2)
    pen.left(18)
    
turtle.done()