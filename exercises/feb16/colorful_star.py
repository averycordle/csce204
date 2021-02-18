#Author: Avery Cordle
import turtle
import random

turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(.5)
pen.hideturtle()
#pen.color("")

colors = ("violet", "indigo", "blue", "green", "yellow", "orange", "red", "teal", "crimson", "medium slate blue", "medium violet red", "cadet blue")


for i in range(100):
    starWidth = random.randint(20,50)
    x = random.randint(int(-turtle.window_width()/2),int(turtle.window_width()/2))
    y = random.randint(int(-turtle.window_height()/2),int(turtle.window_height()/2))
    color = random.choice(colors)
    pen.color(color)

    pen.penup()
    pen.setpos(x,y)
    pen.pendown()

    pen.begin_fill()
    for j in range(3):
        pen.fillcolor(color)
        pen.forward(starWidth)
        pen.left(120)
    pen.end_fill()
    pen.penup()
    pen.setpos(x,y+starWidth/2)
    pen.pendown()
    pen.begin_fill()
    for j in range(3):
        pen.forward(starWidth)
        pen.left(-120)
    pen.end_fill()

turtle.done()