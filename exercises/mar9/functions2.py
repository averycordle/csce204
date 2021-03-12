#Author: Avery Cordle
import turtle
import random

turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.color("black")
pen.fillcolor("blue")
pen.pensize(3)
pen.speed(.5)
pen.hideturtle()

colors = ("violet", "indigo", "blue", "green", "yellow", "orange", "red", "crimson", "medium violet red")

#define positions and cut down code
length = 50
def set_random_position():
    x = random.randint(-int(turtle.window_width()/2), int(turtle.window_width()/2 - length))
    y = random.randint(-int(turtle.window_height()/2), int(turtle.window_height()/2 - length))

    pen.penup()
    pen.setpos(x,y)
    color = random.choice(colors)
    pen.color(color)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor(color)

#define shapes
def draw_square():
    set_random_position()

    for i in range(4):
        pen.forward(length)
        pen.left(90)
    pen.end_fill()

def draw_triangle():
    set_random_position()

    for i in range(3):
        pen.forward(length)
        pen.left(120)
    pen.end_fill()

def draw_star():
    set_random_position

    for i in range(3):
        pen.forward(length)
        pen.left(120)
    pen.end_fill()
    pen.penup()
    pen.setheading(90)
    pen.forward(length/2)
    pen.setheading(0)
    pen.pendown()
    pen.begin_fill()
    for i in range(3):
        pen.forward(length)
        pen.left(-120)
    pen.end_fill()

#call it
for i in range(10):
    choice = random.randint(0,2)
    if choice == 0:
        draw_square()
    elif choice == 1:
        draw_triangle()
    elif choice == 2:
        draw_star()


turtle.done()