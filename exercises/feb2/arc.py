#Author: Avery Cordle
import turtle
#create arcs
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(.5)

#drawing a grid (horizontal line)
pen.penup()
pen.setpos(-turtle.window_width()/2,0)
pen.pendown()
pen.forward(turtle.window_width())
#drawing a grid (horizontal line)
pen.penup()
pen.setheading(270)
pen.setpos(0, turtle.window_height()/2)
pen.pendown()
pen.forward(turtle.window_height())

#smile arc
smileRadius = 100
"""
pen.penup()
pen.setpos(-smileRadius,0)
pen.setheading(-60)
pen.pendown()
pen.circle(smileRadius, 120)
"""
#frown arc
pen.penup()
pen.setpos(-smileRadius,0)
pen.setheading(60)
pen.pendown()
pen.circle(-smileRadius, 120)


turtle.done()