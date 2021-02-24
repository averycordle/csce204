#Author: Avery Cordle

import turtle

turtle.bgcolor("skyblue")
turtle.setup(575,575)
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(.5)

colorList = []
pyramidS = int(turtle.numinput("Pyramid", "Enter Height:",5,1,10))
pyramidSize = int(200/pyramidS)
for i in range(pyramidS):
    color = turtle.textinput("Pyramid",f"Enter color of row {i+1}:").lower().strip()
    colorList.append(color)
    
for row in range(pyramidS):
    x = (-turtle.window_width()/2)/pyramidS + row * pyramidSize/2 
    y = (-turtle.window_height()//2)/pyramidS + row * pyramidSize

    for col in range(pyramidS-row):
        pen.penup()
        pen.setpos(x-pyramidS*(pyramidSize/3.5),y)
        pen.pendown()

        pen.fillcolor(colorList[row])
        pen.begin_fill()
        for i in range(3):
            pen.forward(pyramidSize)
            pen.left(120)
        pen.end_fill()
        x+=pyramidSize

turtle.done()