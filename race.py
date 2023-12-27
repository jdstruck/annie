import turtle
import random

screen = turtle.Screen()


import random
annie=turtle.Turtle()
annie.color('RoyalBlue2')
lucy=turtle.Turtle()
lucy.color('violet')
clara=turtle.Turtle()
clara.color('VioletRed3')

turtles = [annie,lucy,clara]

for turtle in turtles: 
    turtle.penup()
    turtle.shape('turtle')
    turtle.shapesize(5)


annie.goto(-800,200)
lucy.goto(-800,0)
clara.goto(-800,-200)

for race in range(100):
    for turtle in turtles:
        turtle.fd(random.randint(0,30))
    
maxTurt = clara
for turtle in turtles:
    maxx,maxy = maxTurt.pos()
    x,y=turtle.pos()
    print(x)
    if x>maxx:
        maxTurt=turtle
maxTurt.lt(360*5)


screen.exitonclick()