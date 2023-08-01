import turtle
import random

turtle.speed(0)
turtle.bgcolor(0,0,0)
turtle.hideturtle

for i in range(100):
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

    angle = random.randint(0,360)
    turtle.setheading(angle)

    r=random.random()
    g=random.random()
    b=random.random()

    turtle.color(r,g,b)

    turtle.begin_fill()
    size = random.randint(10,50)
    turtle.circle(size,180)
    turtle.right(90)
    turtle.circle(size,180)
    turtle.forward(size*2)
    turtle.left(90)
    turtle.forward(size*2)
    turtle.end_fill()
     

