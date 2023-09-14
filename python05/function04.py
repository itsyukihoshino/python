#function04
import turtle

def draw_star(x, y, color):
    t = turtle.turtles
    t.speed("fastest")
    t.penup()
    t.goto(x,y)
    t.pensize(10)
    t.pencolor(color)
    t.pendown()
    for i in range(80):
        t.forward(i)
        t.left(144)


window = turtle.Screen()
window.setup(800,600)
window.title('function 04')


draw_star(-100,100,"red") #top left corner
draw_star(-100,-100,"blue") #bottom left corner






