import turtle
import random

screen = turtle.Screen()


import random
annie=turtle.Turtle()
annie.color('medium slate blue')
lucy=turtle.Turtle()
lucy.color('cyan')
clara=turtle.Turtle()
clara.color('deep pink')

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
    
maxTurt = annie
for turtle in turtles:
    maxx,maxy = maxTurt.pos()
    x,y=turtle.pos()
    print(x)
    if x>maxx:
        maxTurt=turtle
maxTurt.lt(360*3)


screen.exitonclick()