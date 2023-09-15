#function 06 - Crazy Turtle
import turtle
import random

Window = turtle.Screen()
Window.setup(800, 600)
Window.title('crazy turtle drawing')

t = turtle.Turtle()
t.speed("fastest")

colors = ("light yellow ", "light green", "light blue", "light  pink", "light purple")

for x in range(100):
    t.pencolor(random.choice(colors))
    t.pensize(5)
    t.left(random.randint(0, 360))
    t.forward(random.randint(10, 50))
    


