class House:
    def __init__(self, pen, addy, x, y, width, building_color, roof_color, chimney):
        self.pen=pen
        self.addy=addy
        self.x=x
        self.y=y
        self.width=width
        self.building_color=building_color
        self.roof_color=roof_color
        self.chimney=chimney
        self.style=("Arial", int(width/4), "bold")

    def draw(self):
        self.pen.penup()
        self.pen.setpos(self.x,self.y)
        self.pen.pendown()
        self.draw_house_base()
        self.draw_chimney()
        self.draw_roof()
        self.draw_door()
        self.bay_windows()
        self.draw_doorknob()
        self.write_address()

    def draw_house_base(self):
        self.pen.fillcolor(self.building_color)
        self.pen.begin_fill()
        for i in range(4):
            self.pen.forward(self.width)
            self.pen.left(90)
        self.pen.end_fill()

    def draw_roof(self):
        roof_width = self.width*1.2
        self.pen.penup()
        self.pen.setpos(self.x-self.width*.1,self.y+self.width)
        self.pen.pendown()
        self.pen.fillcolor(self.roof_color)
        self.pen.begin_fill()
        for i in range(3):
            self.pen.forward(roof_width)
            self.pen.left(120)
        self.pen.end_fill()

    def draw_chimney(self):
        if self.chimney:
            chimney_width = self.width*.3
            chimney_height = self.width*.5
            self.pen.penup()
            self.pen.setpos(self.x+self.width*.15,self.y+self.width*1.3)
            self.pen.pendown()
            self.pen.fillcolor(self.building_color)
            self.pen.begin_fill()
            for i in range(4):
                if i%2 ==0:
                    self.pen.forward(chimney_width)
                else: 
                    self.pen.forward(chimney_height)
                self.pen.left(90)
            self.pen.end_fill()

    def draw_door(self):
        door_width = self.width*.4
        door_height = self.width*.6
        self.pen.penup()
        self.pen.setpos(self.x+self.width/3.3,self.y)
        self.pen.pendown()
        self.pen.fillcolor(self.roof_color)
        self.pen.begin_fill()
        for i in range(4):
            if i%2 ==0:
                self.pen.forward(door_width)
            else: 
                self.pen.forward(door_height)
            self.pen.left(90)
        self.pen.end_fill()

    def draw_doorknob(self):
        door_knob_width = self.width*.06
        self.pen.penup()
        self.pen.setpos(self.x+self.width/1.7,self.y+self.width/3.5)
        self.pen.pendown()
        self.pen.fillcolor(self.building_color)
        self.pen.begin_fill()
        self.pen.circle(door_knob_width)
        self.pen.end_fill()

    def bay_windows(self):
        window_width = self.width*.2
        window_height = self.width*.4
        self.pen.penup()
        self.pen.setpos(self.x+self.width/3.3,self.y+self.width/1.4)
        self.pen.pendown()
        self.pen.fillcolor("sky blue")
        self.pen.begin_fill()
        for i in range(4):
            if i%2 ==0:
                self.pen.forward(window_height)
            else: 
                self.pen.forward(window_width)
            self.pen.left(90)
        self.pen.end_fill()

    def write_address(self):
        self.pen.penup()
        self.pen.setpos(self.x,self.y-self.width*.3)
        self.pen.pendown()
        self.pen.write(self.addy)




    
