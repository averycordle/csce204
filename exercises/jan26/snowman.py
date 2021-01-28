#Author: Avery Cordle
import turtle
turtle.bgcolor("skyblue")
turtle.setup(500,500)

#setup pen
pen = turtle.Turtle()
pen.color("black")
pen.fillcolor("white")
pen.speed(.5)
pen.hideturtle()

#input
size = turtle.numinput("Snowman", "Size (1-4): " ,3,1,4)
lgRadius = size *20
medRadius = size *15
smRadius = size *10
eyeRadius = size *2
noseSize = size *4

#draw large circle
pen.penup()
pen.setpos(0, -1.75*lgRadius)
pen.pendown()
pen.begin_fill()
pen.circle(lgRadius)
pen.end_fill()

#draw medium circle
pen.penup()
pen.setpos(0, -.25*lgRadius)
pen.pendown()
pen.begin_fill()
pen.circle(medRadius)
pen.end_fill()

#draw small circle
pen.penup()
pen.setpos(0, lgRadius)
pen.pendown()
pen.begin_fill()
pen.circle(smRadius)
pen.end_fill()

#draw left eye
pen.penup()
pen.setpos(-.4*smRadius, 1.4*lgRadius)
pen.pendown()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(eyeRadius)
pen.end_fill()

#draw right eye
pen.penup()
pen.setpos(.4*smRadius, 1.4*lgRadius)
pen.pendown()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(eyeRadius)
pen.end_fill()

#draw nose
pen.penup()
pen.setpos(0, 1.2*lgRadius)
pen.pendown()
pen.fillcolor("orange")
pen.begin_fill()
pen.setheading(60)
pen.forward(noseSize)
pen.left(120)
pen.forward(noseSize)
pen.left(120)
pen.forward(noseSize)
pen.end_fill()


turtle.done()