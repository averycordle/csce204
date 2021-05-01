#Author: Avery Cordle


class Man:
    def __init__(self, width, appendage):
        self.width = width
        self.appendage = appendage
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
            self.write_message(pen)
        
    def draw_head(self, pen):
        pen.circle(self.width/2)

    def draw_torso(self, pen):
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

    def draw_l_leg(self, pen):
        pen.penup()
        pen.setpos(0,25)
        pen.setheading(315)
        pen.pendown()
        pen.forward(self.width/2)
        pen.setheading(0)

    def write_message(self, pen):
        pen.penup()
        pen.setpos(-50, -50)
        pen.pendown()
        pen.write("Sorry, you lost :(", font=self.style)



    
#draw method "if appendages == 0, don't draw anything; if appendages  == 1, just draw a head; if == 2, draw a head and part of the body"
