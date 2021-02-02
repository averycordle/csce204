#Author: Avery Cordle
import turtle

turtle.bgcolor("white")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(.5)
pen.color("black")

#set variables
grade = turtle.numinput("Grades", "Enter Grade: ");
faceRadius = 200
#make the face
pen.penup()
pen.setpos(0,-faceRadius)
pen.pendown()
pen.circle(faceRadius)
#make the left eye
pen.penup()
pen.setpos(-faceRadius/4, faceRadius/7)
pen.setheading(0)
pen.fillcolor("black")
pen.begin_fill()
pen.pendown()
pen.circle(faceRadius/10)
pen.end_fill()
#make the right eye
pen.penup()
pen.setpos(faceRadius/4, faceRadius/7)
pen.setheading(0)
pen.fillcolor("black")
pen.begin_fill()
pen.pendown()
pen.circle(faceRadius/10)
pen.end_fill()
#if statements
#smile
if grade >=80:
    pen.penup()
    pen.setpos(-faceRadius/2.2, -faceRadius/3)
    pen.setheading(-60)
    pen.pendown()
    pen.circle(faceRadius/2, 120)
#neutral
elif grade >= 70:
    pen.penup()
    pen.setpos(-faceRadius/3, -faceRadius/3)
    pen.setheading(0)
    pen.pendown()
    pen.forward(faceRadius/1.5)
#frown
elif grade <70:
    pen.penup()
    pen.setpos(-faceRadius/2.2, -faceRadius/2)
    pen.setheading(240)
    pen.pendown()
    pen.circle(faceRadius/2, -120)
turtle.done()