#Author: Avery Cordle
from truck import Truck

import turtle

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

#this function will make the street and small yellow street marks
def draw_rectangle(x, y, height, width, color):
    pen.penup()
    pen.setpos(x,y)
    pen.pendown()
    pen.fillcolor(color)

    pen.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            pen.forward(width)
        else:
            pen.forward(height)
        pen.left(90)
    pen.end_fill()
#draw the street
draw_rectangle(-turtle.window_width()/2,-turtle.window_height()/8, turtle.window_height()/4, turtle.window_width(), "gray")
x=0
for i in range(5):
    draw_rectangle(x-turtle.window_width()/2,0/-turtle.window_height()/60, turtle.window_height()/30, turtle.window_width()/6, "yellow")
    x+=turtle.window_width()/5
    
trucks = []
trucks.append(Truck(-265, 70, 20, "medium aquamarine", False, True,))
trucks.append(Truck(-145, 70, 20, "plum", True, False,))
trucks.append(Truck(-50, 70, 20, "skyblue", True, True,))
trucks.append(Truck(80, 70, 20, "orchid", False, False,))
trucks.append(Truck(180, 70, 20, "lime", True, True,))

for truck in trucks:
    truck.draw(pen)

turtle.done()