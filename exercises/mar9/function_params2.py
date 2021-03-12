#Author: Avery Cordle

import turtle
import random

turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(.5)
pen.hideturtle()
"""
pen.penup()
pen.pendown()
"""

def draw_rec(x,y,width,length,color):
    x = random.randint(int(-turtle.window_width()/2), int(turtle.window_width()/2))
    y = random.randint(int(-turtle.window_height()/2), int(turtle.window_height()/2))
    pen.penup()
    pen.setpos(x,y)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor(color)
    for i in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(length)
        pen.left(90)
    pen.end_fill()

def draw_square(x,y,width,color):
    draw_rec(x,y,width,width,color)

def draw_triangle(x,y,width,color):
    x = random.randint(int(-turtle.window_width()/2), int(turtle.window_width()/2))
    y = random.randint(int(-turtle.window_height()/2), int(turtle.window_height()/2))
    pen.penup()
    pen.setpos(x,y)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor(color)
    for i in range(3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()

for i in range(10):
    draw_triangle(50, 100, 50, "pink")

for i in range(10):
    draw_rec(50,100,100,50,"yellow")

for i in range(10):
    draw_square(50, 100, 50, "blue")

turtle.done()