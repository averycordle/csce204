#Author: Avery Cordle

import turtle

turtle.bgcolor("skyblue")
turtle.setup(575,575)
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(.5)
pen.hideturtle()

gridSize = int(turtle.numinput("Circles", "How many circles do you want?", 5,1,10))

diameterPadding = turtle.window_width()/gridSize
radius = diameterPadding * .8 / 2
padding = diameterPadding * .1

for row in range(gridSize):
    x = -turtle.window_width()/2 + diameterPadding/2
    y = -turtle.window_height()/2 + padding + diameterPadding *row
    

    pen.penup()
    pen.setpos(x,y)
    pen.pendown()
    pen.circle(radius)
    

    for col in range(gridSize):
        pen.penup()
        pen.setpos(x + diameterPadding * col,y)
        pen.pendown()
        pen.circle(radius)
        # OR YOU CAN DO THIS INSTEAD OF "+ diameterPadding * col": x += diameterPadding










turtle.done()