#Author: Avery Cordle

import turtle

turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(.5)
pen.hideturtle()
#pen.color("")

colors = ("violet", "indigo", "blue", "green", "yellow", "orange", "red")
radius =100
counter = 0

for color in colors:
    pen.penup()
    pen.setpos(-radius/2,counter*10)
    pen.pendown()
    pen.setheading(60)
    pen.color(color)
    pen.circle(-radius,120)
    counter+=1


turtle.done()