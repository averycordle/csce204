def draw_rect(pen, x, y, width, height):
    pen.penup()
    pen.setpos(x,y)
    pen.pendown()
    for i in range(4):
        if i%2== 0:
            pen.forward(width)
        else:
            pen.forward(height)
        pen.left(90)

def draw_square(pen, x, y, width):
    draw_rect(pen, x, y, width, width)

def draw_tri(pen, x, y, length):
    pen.penup()
    pen.setpos(x,y)
    pen.pendown()
    for i in range(3):
        pen.forward(length)
        pen.left(120)