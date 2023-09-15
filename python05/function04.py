#function04
import turtle

def draw_star(x, y, color):
    t = turtle.turtles
    turtle.speed("fastest")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pensize(10)
    turtle.pencolor(color)
    turtle.pendown()
    for i in range(80):
        turtle.forward(i)
        turtle.left(144)


window = turtle.Screen()
window.setup(800,600)
window.title('function 04')





window.exitonclick()


