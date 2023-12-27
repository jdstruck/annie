import turtle

screen = turtle.Screen()

turtle.speed('fastest')
turtle.hideturtle()
turtle.width(5)

def draw_egg(rad):
    for i in range(2):
        turtle.circle(rad,90)
        turtle.circle(rad//2,90)

def visible_baby_turtle(pos):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed('fastest')
    t.color('SeaGreen4')
    t.shape('turtle')
    t.shapesize(5)
    t.penup()
    t.goto(pos)
    t.lt(90)
    t.fd(80)
    t.lt(90)
    t.fd(50)
    t.rt(90)
    t.speed('slowest')
    t.showturtle()
   # t.fd(100)



def invisible_turtle(pos):
    t = turtle.Turtle()
    t.hideturtle()
    turtle.speed('fastest')
    t.shape("circle")
    t.shapesize(8)
    t.color('white')
    t.penup()
    t.goto(pos)
    t.lt(90)
    t.fd(80)
    t.lt(90)
    t.fd(50)
    t.showturtle()


for i in range(3):
    turtle.seth(45)
    draw_egg(150)
    visible_baby_turtle(turtle.pos())
    invisible_turtle(turtle.pos())
    turtle.penup()
    turtle.seth(0)
    turtle.fd(205)
    turtle.pendown()

screen.exitonclick()