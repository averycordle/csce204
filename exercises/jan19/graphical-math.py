#Author: Avery Cordle
import turtle
#relativity
turtle.bgcolor("skyblue")
turtle.setup(500,500)

#set up pen
pen = turtle.Turtle()
pen.color("black")
pen.fillcolor("white")

#define the size
#turtle.numinput("Title", "Prompt", "default", "min", "max")
size = turtle.numinput("Snowman", "Size (1-4): ",3,1,4)
lgRadius = size * 20

#draw the bottome circle
pen.penup()
pen.setpos(0,-100)
pen.pendown()
pen.begin_fill()
pen.circle(lgRadius)
pen.end_fill()


turtle.done()