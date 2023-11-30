import turtle
import random
turtle.speed(0)
turtle.width(5)
turtle.colormode(255)

for p in range (44):
    turtle.pencolor(random.randint(1,200),random.randint(10,20),random.randint(1,255))
    turtle.rt(125)
    for s in range (36):
        turtle.lt(10)
        turtle.fd(20)
