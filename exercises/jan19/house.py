import turtle
turtle.bgcolor("skyblue")
#setting up our pen
pen = turtle.Turtle()
pen.pensize(5)
pen.speed(.5)
pen.color("black")

#draw the house
pen.setpos(-100,-100)
pen.fillcolor("yellow")
pen.begin_fill()
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.end_fill()


#draw the roof
pen.penup()
pen.setpos(-100,100)
pen.setheading(0)
pen.fillcolor("red")
pen.begin_fill()
pen.pendown()
pen.forward(200)
pen.left(120)
pen.forward(200)
pen.left(120)
pen.forward(200)

pen.end_fill()

#draw the door
pen.penup()
pen.setpos(25,-100)
pen.setheading(90)
pen.fillcolor("blue")
pen.begin_fill()
pen.down()
pen.forward(75)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(75)
pen.left(90)
pen.forward(50)
pen.end_fill()

#draw the doorknob
pen.penup()
pen.setpos(15,-60)
pen.fillcolor("green")
pen.begin_fill()
pen.pendown()
pen.circle(5)
pen.end_fill()

#windows -left
pen.penup()
pen.setpos(-75,25)
pen.fillcolor("skyblue")
pen.begin_fill()
pen.pendown()
pen.forward(30)
pen.left(90)
pen.forward(30)
pen.left(90)
pen.forward(30)
pen.left(90)
pen.forward(30)
pen.end_fill()

#window cross -left
pen.penup()
pen.setpos(-60,25)
pen.pencolor("black")
pen.setheading(90)
pen.pendown()
pen.forward(30)
pen.penup()
pen.setpos(-75,40)
pen.pencolor("black")
pen.setheading(0)
pen.pendown()
pen.forward(30)

#windows -right
pen.penup()
pen.setpos(50,25)
pen.setheading(0)
pen.fillcolor("skyblue")
pen.begin_fill()
pen.pendown()
pen.forward(30)
pen.left(90)
pen.forward(30)
pen.left(90)
pen.forward(30)
pen.left(90)
pen.forward(30)
pen.end_fill()

#window cross -right
pen.penup()
pen.setpos(65,25)
pen.pencolor("black")
pen.setheading(90)
pen.pendown()
pen.forward(30)
pen.penup()
pen.setpos(50,40)
pen.pencolor("black")
pen.setheading(0)
pen.pendown()
pen.forward(30)

#grass
pen.penup()
pen.setpos(-200,-100)
pen.pencolor("green")
pen.setheading(0)
pen.pendown()
pen.forward(400)

turtle.done()