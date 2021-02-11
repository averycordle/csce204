#Author: Avery Cordle
import turtle
import random

turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(.5)
pen.color("black")
style = ("Arial", 12, "normal")
pen.hideturtle()
turtle.colormode(255)

numNames = turtle.numinput("Name", "Number of Names", 10,1,100)

#loop and draw the user's name

for i in range(int(numNames)):
    x = random.randint(int(-turtle.window_width()/2),int(turtle.window_width()/2))
    y = random.randint(int(-turtle.window_height()/2),int(turtle.window_height()/2))
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    pen.color(red,green,blue)
    pen.penup()
    pen.setpos(x,y)
    pen.pendown()
    pen.write("Avery", font = style)
turtle.done()