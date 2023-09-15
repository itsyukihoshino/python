#function05 - Draw stars at random
import turtle
import random
turtle.bgcolor("blue")

def draw_star(x, y, color):
    t = turtle.turtles
    turtle.speed("fastest")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pensize()
    turtle.pencolor(color)
    turtle.pendown()
    for i in range(50):
        turtle.forward(i)
        turtle.left(144)


window = turtle.Screen()
window.setup(800,600)
window.title('function 05')

for count in range(50):
    draw_star(random.randint(-400, 400), random.randint(-300, 300), "yellow")