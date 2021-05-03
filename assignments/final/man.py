#Author: Avery Cordle
class Man:
    def __init__(self, width, appendage, outcome):
        self.width = width
        self.appendage = appendage
        self.outcome = outcome
        self.style = ("Courier",20)

    def draw(self, pen):
        pen.penup()
        pen.setpos(0,75)
        pen.pendown()
        
        if self.appendage == 1:
            self.draw_head(pen)
        elif self.appendage == 2:
            self.draw_torso(pen)
        elif self.appendage == 3:
            self.draw_r_arm(pen)
        elif self.appendage == 4:
            self.draw_l_arm(pen)
        elif self.appendage == 5:
            self.draw_r_leg(pen)
        elif self.appendage == 6:
            self.draw_l_leg(pen)
            self.write_lose_message(pen)
        if self.outcome == 1:
            self.write_win_message(pen)
        
    def draw_head(self, pen):
        pen.circle(self.width/2)
        pen.penup()
        pen.setpos(-150, -50)
        pen.pendown()
        pen.write("Don't sweat it!", font=self.style)
        pen.setheading(0)

    def draw_torso(self, pen):
        self.coverup(pen)
        pen.penup()
        pen.setpos(0,75)
        pen.setheading(270)
        pen.pendown()
        pen.forward(self.width)
        pen.setheading(0)

    def draw_r_arm(self, pen):
        pen.penup()
        pen.setpos(0,55)
        pen.setheading(180)
        pen.pendown()
        pen.forward(self.width/2)
        pen.setheading(0)

    def draw_l_arm(self, pen):
        pen.penup()
        pen.setpos(0,55)
        pen.pendown()
        pen.forward(self.width/2)

    def draw_r_leg(self, pen):
        pen.penup()
        pen.setpos(0,25)
        pen.setheading(225)
        pen.pendown()
        pen.forward(self.width/2)
        pen.penup()
        pen.setpos(-250, -50)
        pen.pendown()
        pen.write("Be Careful! Only 1 more guess", font=self.style)
        pen.setheading(0)

    def draw_l_leg(self, pen):
        self.coverup(pen)
        pen.penup()
        pen.setpos(0,25)
        pen.setheading(315)
        pen.pendown()
        pen.forward(self.width/2)
        pen.setheading(0)

    def write_win_message(self, pen):
        self.coverup(pen)
        pen.penup()
        pen.setpos(-110, -50)
        pen.pendown()
        pen.write("You Won!", font=self.style)

    def write_lose_message(self, pen):
        pen.penup()
        pen.setpos(-200, -50)
        pen.pendown()
        pen.write("Sorry, you lost :(", font=self.style)

    def coverup(self, pen):
        pen.penup()
        pen.setpos(-255, -50)
        pen.fillcolor("white")
        pen.color("white")
        pen.pendown()
        pen.begin_fill()
        for i in range(4):
            if i%2==0:
                pen.forward(self.width*12)
            else:
                pen.forward(self.width)
            pen.left(90)
        pen.end_fill()
        pen.color("black")