#Author: Avery Cordle
import turtle
import random


turtle.bgcolor("white")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(.5)
pen.hideturtle()
#pen.color("")


pen.penup()
pen.setpos(-turtle.window_width()/2, -turtle.window_height()/2)
pen.pendown()

pen.color("blue")
pen.begin_fill()

#draw the blue

for i in range(4):
    if i % 2 ==0:
        pen.forward(turtle.window_width()/2)
    else:
        pen.forward(turtle.window_height())
    pen.left(90)
pen.end_fill()

pen.color("red")
stripeHeight = turtle.window_height()/13
stripeWidth = turtle.window_width()/2

#draw the stripes

for i in range(0,13,2):
    pen.penup()
    y = -turtle.window_width()/2 + stripeHeight * i #use i here bc it means nothing right now so it will be at 0
    pen.setpos(0, int(y))
    pen.pendown()
    
#draw the rectangle
    pen.begin_fill()
    for j in range(4):
        if j % 2 == 0: #if even
            pen.forward(stripeWidth)
        else:
            pen.forward(stripeHeight)
        pen.left(90)
    pen.end_fill()

#star time

for i in range(50):
    x = random.randint(-int(turtle.window_width()/2),int(0-stripeHeight))
    y = random.randint(-int(turtle.window_height()/2) + int(stripeHeight), int(turtle.window_height()/2) - int(stripeHeight))

    pen.penup()
    pen.setpos(x,y)
    pen.pendown()

    pen.color("white")
    pen.fillcolor("white")
    pen.begin_fill()
    for j in range(3):
        pen.forward(stripeHeight)
        pen.left(120)
    pen.end_fill()
    pen.penup()
    pen.setpos(x,y+stripeHeight/2)
    pen.pendown()
    pen.begin_fill()
    for j in range(3):
        pen.forward(stripeHeight)
        pen.left(-120)
    pen.end_fill()

turtle.done()