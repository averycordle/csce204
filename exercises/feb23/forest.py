#Author: Avery Cordle

import turtle

turtle.bgcolor("skyblue")
turtle.setup(575,575)
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(.5)
pen.hideturtle()

gridSize = int(turtle.numinput("Trees", "How many trees do you want?", 5,1,10))
widthPadding = turtle.window_width()/gridSize
padding = widthPadding * .1
width = widthPadding * .8

stumpWidth = width * .2
stumpHeight = width * .5
leafRadius = width * .5 / 2

for row in range(gridSize):
    x = -turtle.window_width()/2 + widthPadding/2 - stumpWidth/2
    y = -turtle.window_height()/2 + padding + row * widthPadding 


    for col in range(gridSize):

        pen.fillcolor("sienna")
        pen.penup()
        pen.setpos(x,y)
        pen.pendown()

        pen.begin_fill()
        #draw a stump
        for i in range(4):
            if i % 2 == 0:
                pen.forward(stumpWidth)
            else:
                pen.forward(stumpHeight)
            pen.left(90)
        pen.end_fill()


        #draw leaves
        pen.fillcolor("forest green")
        pen.penup()
        pen.setpos(x + stumpWidth/2,y + stumpHeight * .8)
        pen.pendown()
        pen.begin_fill()
        pen.circle(leafRadius)
        pen.end_fill()

        x += widthPadding

turtle.done()