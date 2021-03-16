#Author: Avery Cordle

import turtle
import random

turtle.bgcolor("skyblue")
turtle.setup(525,525)
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(.5)

colors = ("blue", "green", "yellow", "orange", "red", "white")

def draw_square(x,y,width,color):
    pen.penup()
    pen.setpos(x,y)
    pen.pendown()
    pen.begin_fill()
    pen.color("black")
    color = random.choice(colors)
    pen.fillcolor(color)
    for i in range(4):
        pen.forward(size)
        pen.left(90)
    pen.end_fill()

def rubics_cube(x,y,size):
    x = random.randint(int(-turtle.window_width()/2), int(turtle.window_width()/2-size*3))
    y = random.randint(int(-turtle.window_height()/2), int(turtle.window_height()/2-size*3))
    for i in range(3):
        for i in range(3):
            draw_square(x,y,size,colors)
            x+=size
        x-=(size*3)
        y+=size
    
for i in range(10):
    size = random.randint(20,100)
    rubics_cube(10,10,size)

turtle.done()