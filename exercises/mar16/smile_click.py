#Author: Avery Cordle

import turtle

turtle.bgcolor("skyblue")
turtle.setup(575,575)
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(.5)
pen.color("black")
pen.hideturtle()

smileRadius = 50

def draw_smiley(x,y):
    draw_head(x,y)
    draw_eye(x-smileRadius/3,y+smileRadius)
    draw_eye(x+smileRadius/3,y+smileRadius)
    draw_mouth(x-smileRadius/2.5,y+smileRadius/1.5)

def draw_head(x,y):
    pen.penup()
    pen.setpos(x,y)
    pen.pendown()
    pen.fillcolor("yellow")
    pen.begin_fill()
    pen.circle(smileRadius)
    pen.end_fill()

def draw_eye(x,y):
    pen.penup()
    pen.setpos(x,y)
    pen.pendown()
    pen.fillcolor("black")
    pen.begin_fill()
    pen.circle(smileRadius/10)
    pen.end_fill()

def draw_mouth(x,y):
    pen.penup()
    pen.setpos(x,y)
    pen.pendown()
    pen.setheading(-60)
    pen.circle(smileRadius/2, 120)
    pen.setheading(0)

turtle.onscreenclick(draw_smiley) #on screen click automatically passes in the function so we son't have to add (x,y)

turtle.done()