#Author: Avery Cordle
import turtle
turtle.bgcolor("skyblue")
turtle.setup(500,500)

#setup the pen
pen = turtle.Turtle()
pen.color("black")
pen.fillcolor("red")
pen.speed(.5)
pen.hideturtle()

#get the uhaul size
size = turtle.numinput("U-hual", "Size 1-10: " ,5,1,10)
uHaulWidth = size*50
boxWidth = uHaulWidth * .75
cabWidth = uHaulWidth - boxWidth
boxHeight = uHaulWidth/3
cabHeight = boxHeight/1.5
tireRadius = uHaulWidth * .1

#draw the uHaul 
pen.penup()
pen.setpos(-uHaulWidth/2,0)
pen.pendown()
pen.begin_fill()
pen.forward(uHaulWidth)

pen.left(90)
pen.forward(cabHeight)

pen.left(90)
pen.forward(cabWidth)

pen.right(90)
pen.forward(boxHeight-cabHeight)

pen.left(90)
pen.forward(boxWidth)

pen.left(90)
pen.forward(boxHeight)
pen.end_fill()

#make the wheels
pen.penup()
pen.setheading(360)
pen.setpos(-uHaulWidth/4,-tireRadius*2)
pen.pendown()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(tireRadius)
pen.end_fill()

pen.penup()
pen.setpos(uHaulWidth/4,-tireRadius*2)
pen.pendown()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(tireRadius)
pen.end_fill()

turtle.done()