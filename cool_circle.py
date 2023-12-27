import turtle
import random
screen = turtle.Screen()
turtle.speed(0)
turtle.width(5)
turtle.colormode(255)

for p in range (44):
    turtle.pencolor(random.randint(25,200),random.randint(10,20),random.randint(50,255))
    turtle.rt(125)
    for s in range (36):
        turtle.lt(10)
        turtle.fd(20)

screen.exitonclick()