#Author: Avery Cordle

import turtle

turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(.5)
pen.color("black")
pen.fillcolor("green")

size = 200
bottomTree = size
middleTree = size/2
topTree = size/3
stemSize = size/1.5




#draw
#bottom tree
pen.penup()
pen.setpos(-size/2,-size/2.75)
pen.pendown()

pen.begin_fill()
for i in range(3):
    pen.forward(bottomTree)
    pen.left(120)
pen.end_fill()    

#middle tree
pen.penup()
pen.setpos(-size/4,size/4)
pen.pendown()

pen.begin_fill()
for i in range(3):
    pen.forward(middleTree)
    pen.left(120)
pen.end_fill()  

#top tree
pen.penup()
pen.setpos(-size/6,size/1.75)
pen.pendown()

pen.begin_fill()
for i in range(3):
    pen.forward(topTree)
    pen.left(120)    
pen.end_fill()  

#star on top

pen.penup()
pen.setpos(-size/20,size/1.15)
pen.pendown()

pen.color("gold")
pen.fillcolor("gold")
pen.begin_fill()

for i in range(3):
    pen.forward(size/10)
    pen.left(120)
pen.end_fill() 

pen.penup()
pen.setpos(-size/20,size/1.09)
pen.pendown()

pen.color("gold")
pen.fillcolor("gold")
pen.begin_fill()

for i in range(3):
    pen.forward(size/10)
    pen.left(-120)
pen.end_fill() 

#trunk
pen.penup()
pen.setpos(-size/8,-size/2.75)
pen.pendown()

pen.color("black")
pen.fillcolor("brown")
pen.begin_fill()
for i in range(4):
    pen.forward(size/4)
    pen.left(-90)
pen.end_fill() 



turtle.done()