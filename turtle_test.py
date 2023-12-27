import turtle
turtle.shape("turtle")
turtle.width(15)
turtle.shapesize(17)
screen = turtle.Screen()

length = 400
angle = 90

colors = ['purple', 'yellow','green','blue']

for color in colors:
    turtle.color(color)
    turtle.fd(length)
    turtle.rt(angle)

screen.exitonclick()