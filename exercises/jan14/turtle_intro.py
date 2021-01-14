#Author: Avery Cordle
import turtle
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.pensize(5)

#draw a circle
pen.circle(30)
pen.up()
pen.setpos(100,200)
pen.down()
pen.circle(40)

#draw a square
pen.up()
pen.setpos(-100,100)
pen.down()
pen.forward(100)



turtle.done()