from house import House
import turtle

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

myHouses= (
    House(pen, "1 A Street", -200, 0, 50, "medium aquamarine", "hot pink", True),
    House(pen, "2 A Street", -100, 0, 50, "cyan", "burlywood", False),
    House(pen, "3 A Street", 0, 0, 50, "medium orchid", "lime", True),
    House(pen, "4 A Street", 100, 0, 50, "sandy brown", "aquamarine", True),
    House(pen, "5 A Street", 200, 0, 50, "light sky blue", "plum", False),

    House(pen, "1 B Street", -250, -100, 50, "medium aquamarine", "hot pink", True),
    House(pen, "2 B Street", -150, -100, 50, "cyan", "burlywood", True),
    House(pen, "3 B Street", -50, -100, 50, "medium orchid", "lime", False),
    House(pen, "4 B Street", 50, -100, 50, "sandy brown", "aquamarine", True),
    House(pen, "5 B Street", 150, -100, 50, "light sky blue", "plum", False)


)

for house in myHouses:
    house.draw()










turtle.done()