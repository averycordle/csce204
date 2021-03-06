#Author: Avery Cordle
import turtle
import random

turtle.bgcolor("white")
turtle.setup(700,700)
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(.5)

#list section
numDays = int(turtle.numinput("Forecast", "Enter how many days you would like to forecast (1-10 days): ", 7, 0, 10))
weatherCondition = []
weatherTemp = []
weatherSeven = []
weatherOpinion = []

#size section
shapeSize = 100/numDays
widthPadding = turtle.window_width()/numDays
heightPadding = turtle.window_height()
style = 200/numDays
style2 = ("Arial", 32, "normal")

#loop section
for i in range(numDays):
    userInput1 = turtle.textinput("Days of Forecast","Enter day name (m)onday, (t)uesday, (w)ednesday, (th)ursday, (f)riday, (sa)turday, or (su)nday: ").lower().strip()
    weatherSeven.append(userInput1)

    for i in range(1):
        userInput2 = turtle.textinput("Weather Condition","Describe the weather condition (s)unny, (r)aining, (w)indy, (sn)owing, (st)ormy: ").lower().strip()
        weatherCondition.append(userInput2)

        for i in range(1):
            userInput3 = turtle.numinput("Weather Temperature","Enter the temperature in fahrenheit: ", 70,-50,150)
            weatherTemp.append(userInput3)

            for i in range(1):
                userInput4 = turtle.textinput("Weather Opinion","Do you like today's weather? (y)es, (n)o, (o)kay ").lower().strip()
                weatherOpinion.append(userInput4)

#make the backgrounds (weatherCondition)
x=-turtle.window_width()/2
y=-turtle.window_height()/2

for condition in weatherCondition:
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.begin_fill()
    #sunny
    if condition == "s":
        pen.color("blue")
    #rainy
    elif condition == "r":
        pen.color("gray")
    #windy
    elif condition == "w":
        pen.color("light blue")   
    #snowy 
    elif condition == "sn":
        pen.color("light gray")
    #stormy
    else:
        pen.color("gray")
    for i in range(4):
        if i % 2 == 0:
            pen.forward(widthPadding)
        else:
            pen.forward(heightPadding)
        pen.left(90)
    pen.end_fill()
    x+=widthPadding

#draw the details (weatherCondition part2)
x=-turtle.window_width()/2
y=-turtle.window_height()/2

for condition in weatherCondition:
    #sun
    if condition == "s":
        pen.penup()
        pen.setpos(x+widthPadding/2,y+heightPadding/2)
        pen.pendown()
        pen.setheading(180)
        pen.color("yellow")
        for i in range(20):
            pen.forward(shapeSize/1.5)
            pen.left(180)
            pen.forward(shapeSize/1.5)
            pen.left(18)
    #rain drops
    elif condition == "r":
        for i in range(20):
            rainX = random.randint(int(x+shapeSize/2), int(x+widthPadding-shapeSize/2))
            rainY = random.randint(int(y+shapeSize/2),int(y+heightPadding-shapeSize/2))
            pen.penup()
            pen.setpos(rainX, rainY)
            pen.down()
            pen.color("light blue")
            pen.begin_fill()
            pen.circle(shapeSize/4)
            pen.end_fill()
    #wind
    elif condition == "w":
        for i in range(20):
            windX = random.randint(int(x+shapeSize/2), int(x+widthPadding-shapeSize/2))
            windY = random.randint(int(y+shapeSize/2),int(y+heightPadding-shapeSize/2))
            pen.penup()
            pen.setpos(windX, windY)
            pen.down()
            pen.color("gray")
            pen.setheading(45)
            pen.forward(shapeSize/4)
    #snow flakes
    elif condition == "sn":
        for i in range(20):
            snowX = random.randint(int(x+shapeSize/2), int(x+widthPadding-shapeSize))
            snowY = random.randint(int(y+shapeSize/2),int(y+heightPadding-shapeSize))
            pen.penup()
            pen.setpos(snowX, snowY)
            pen.down()
            pen.color("white")
            for i in range(9):
                pen.forward(shapeSize/1.5)
                pen.left(180)
                pen.forward(shapeSize/1.5)
                pen.left(18)
    #lightning
    else:
        pen.penup()
        pen.setpos(x+widthPadding/2,y+heightPadding/2)
        pen.pendown()
        pen.setheading(180)
        pen.color("yellow")
        pen.setpos(x+widthPadding/2-shapeSize/2,y+heightPadding/2)
        pen.begin_fill()
        for i in range(3):
            pen.forward(-shapeSize)
            pen.left(-120)
        pen.end_fill()
        pen.penup()
        pen.setpos(x+widthPadding/2,y+heightPadding/2-shapeSize/2)
        pen.pendown()
        pen.begin_fill()
        for i in range(3):
            pen.forward(-shapeSize)
            pen.left(-120)
        pen.end_fill()
        #cloud
        pen.penup()
        pen.setpos(x+widthPadding/2,y+heightPadding/2+shapeSize)
        pen.pendown()
        pen.begin_fill()
        pen.color("purple")
        pen.circle(shapeSize/2)
        pen.end_fill()
        for i in range(2):
            pen.penup()
            pen.setpos(x+widthPadding/2-shapeSize/1.5,y+heightPadding/2+shapeSize-shapeSize/3)
            pen.pendown()
            pen.begin_fill()
            pen.color("purple")
            pen.circle(shapeSize/2)
            pen.end_fill()
            x+=shapeSize*1.3
        x-=shapeSize*2.6
    x+=widthPadding

#Title will be Weather Report
w = -turtle.window_width()/2.1
z = turtle.window_height()/2.5
turtle.penup()
turtle.setpos(w,z)
turtle.pendown()
turtle.write("Weather Report", font = style2)

#write the day of the week (weatherSeven)
if numDays == 1:
    x = -turtle.window_width()/2 + widthPadding/2
else:
    x = -turtle.window_width()/2 + widthPadding/numDays/1.6 + style/2
y = turtle.window_height()/4 
for weekDay in weatherSeven:
    turtle.up()
    turtle.setpos(x,y)
    turtle.down()
    if weekDay == "m":
        turtle.write("Monday")
    elif weekDay == "t":
        turtle.write("Tuesday")
    elif weekDay == "w":
        turtle.write("Wednesday")
    elif weekDay == "th":
        turtle.write("Thursday")
    elif weekDay == "f":
        turtle.write("Friday")
    elif weekDay == "sa":
        turtle.write("Saturday")
    else:
        turtle.write("Sunday")
    x+=widthPadding

#write the temperature
if numDays == 1:
    x = -turtle.window_width()/2 + widthPadding/2
else:
    x = -turtle.window_width()/2 + widthPadding/numDays/1.6 + style/2
y = turtle.window_height()/4 -heightPadding/8
counter=0
for temp in weatherTemp:
    turtle.up()
    turtle.setpos(x,y)
    turtle.down()
    turtle.write(weatherTemp[counter])
    counter+=1
    x+=widthPadding

#draw the opinion
if numDays == 1:
    x = -turtle.window_width()/2 + widthPadding/2 
else:
    x = -turtle.window_width()/2 + widthPadding/numDays/1.6 
y = turtle.window_height()/4 -heightPadding/2

for opinion in weatherOpinion:
    #make the left eye
    pen.penup()
    pen.setpos(x,y)
    pen.setheading(0)
    pen.color("black")
    pen.fillcolor("black")
    pen.begin_fill()
    pen.pendown()
    pen.circle(shapeSize/10)
    pen.end_fill()
    #make the right eye
    pen.penup()
    pen.setpos(x+shapeSize,y)
    pen.setheading(0)
    pen.fillcolor("black")
    pen.begin_fill()
    pen.pendown()
    pen.circle(shapeSize/10)
    pen.end_fill()
    #if statements
    #smile
    if opinion == "y":
        pen.penup()
        pen.setpos(x,y-shapeSize/2)
        pen.setheading(-60)
        pen.pendown()
        pen.circle(shapeSize/2, 120)
    #neutral
    elif opinion == "o":
        pen.penup()
        pen.setpos(x,y-shapeSize/2)
        pen.setheading(0)
        pen.pendown()
        pen.forward(shapeSize)
    #frown
    elif opinion == "n":
        pen.penup()
        pen.setpos(x,y-shapeSize/2)
        pen.setheading(240)
        pen.pendown()
        pen.circle(shapeSize/2, -120)
    x+=widthPadding

turtle.done()