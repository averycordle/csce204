#Author: Avery Cordle
#load the turtle
import turtle
turtle.bgcolor("white")
turtle.setup(450,450)
pen = turtle.Turtle()
pen.speed(.5)
pen.color("black")
#ask the user
size = turtle.numinput("Olympic Circle", "Size (1-10): ",5,1,10)
rRadius = size * 6
pen.pensize(size)
#black ring
pen.penup()
pen.setpos(0,0)
pen.pendown()
pen.circle(rRadius)
#blue ring
pen.penup()
pen.setx(-2.5*rRadius)
pen.color("blue")
pen.pendown()
pen.circle(rRadius)
#red ring
pen.penup()
pen.setx(2.5*rRadius)
pen.color("red")
pen.pendown()
pen.circle(rRadius)
#gold ring
pen.penup()
pen.setx(-1.25*rRadius)
pen.sety(-1.25*rRadius)
pen.color("gold")
pen.pendown()
pen.circle(rRadius)
#green ring
pen.penup()
pen.setx(1.25*rRadius)
pen.sety(-1.25*rRadius)
pen.color("green")
pen.pendown()
pen.circle(rRadius)
turtle.done()