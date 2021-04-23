import turtle

import shapes as sh

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

sh.draw_square(pen, -50, -50, 100)
sh.draw_tri(pen,-60,50,120)
sh.draw_rect(pen,-10,-50,20,40)









turtle.done()