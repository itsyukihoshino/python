import turtle
import time

def left():
    print(left)

def right():
    print(right)

#enable and register keyboard events
turtle.listen() 
turtle.onkey(left, left)
turtle.onkey(right, right)

win = turtle.Screen()
win.title("SPACE SHIP VS WITH UFOS")
win.setup(800, 600)
win.bgpic("space-bg.gif")
win.tracer(0)

#register graphic with turtle graphics
turtle.register_shape("ship.gif")

#create a turtle for my ship
spaceship = turtle.Turtle()
spaceship.shape("ship.gif")
spaceship.penup()
spaceship.speed(0)
spaceship.goto(0, -200)

moveShipBy = 3

#game loop that redraws our screen each time the loop executes
while Ture:

    spaceship.forward(moveShipby)

    win.update()