class Truck:
    def __init__(self, x, y, height, color, extended_cab, xlong_bed):
        self.x = x
        self.y = y
        self.height = height
        self.color = color
        self.extended_cab = extended_cab
        self.xlong_bed = xlong_bed

    def draw(self, pen):
        pen.penup()
        pen.setpos(self.x-self.height/2, self.y-self.height/2)
        pen.pendown()
        pen.fillcolor(self.color)

        #draw the basic cab
        self.draw_truck_body(pen)
        #draw the top of the cab
        self.draw_truck_cab(pen)
        #draw the wheels
        self.draw_wheels(pen)
    
    #basic cab
    def draw_truck_body(self, pen):
        if self.xlong_bed:
            width = self.height*5
        else: 
            width = self.height*4
        self.draw_rect(pen, width, self.height, self.color)

    #top of the cab
    def draw_truck_cab(self, pen):
        pen.penup()
        pen.setpos(self.x+self.height*.4, self.y+self.height/2)
        pen.pendown()
        #for extended_cab = True
        if self.extended_cab:
            width = self.height*1.5
            window_space = 0
            self.draw_rect(pen, width, self.height, self.color)
            #the windows
            for i in range(2):
                pen.penup()
                pen.setpos(self.x+width*.5 + window_space, self.y+self.height/2)
                pen.pendown()
                self.draw_rect(pen, width/5, self.height/1.5, "white")
                window_space += width/3
            
        #for extended_cab = False
        else:
            width = self.height
            self.draw_rect(pen, width, self.height, self.color)
            #the window
            pen.penup()
            pen.setpos(self.x+self.height*.6, self.y+self.height/2)
            pen.pendown()
            self.draw_rect(pen, width/3, self.height/1.5, "white")

    #wheels
    def draw_wheels(self, pen):
        for i in range(2):
            pen.penup()
            pen.setpos(self.x+self.height/2, self.y-self.height)
            pen.fillcolor("black")
            pen.begin_fill()
            pen.pendown()
            pen.circle(self.height/3)
            pen.end_fill()
            if self.xlong_bed:
                self.x+=self.height*3
            else:
                self.x+=self.height*2

#draw rectangle method to copy and paste less
    def draw_rect(self, pen, width, height, color):
        pen.fillcolor(color)
        pen.begin_fill()
        for i in range(4):
            if i % 2 == 0:
                pen.forward(width)
            else:
                pen.forward(height)
            pen.left(90)
        pen.end_fill()
 