import turtle
import time
import os


def left():
    print("Moving left")

def right():
    print("Moving right")
# Change the working directory to where the script is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

 
turtle.listen() 
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")

win = turtle.Screen()
win.title("SPACE SHIP VS WITH UFOS")
win.setup(800, 600)
win.bgpic("space-bg.gif")
win.tracer(0)


turtle.register_shape("ship.gif")


spaceship = turtle.Turtle()
spaceship.shape("ship.gif")
spaceship.penup()
spaceship.speed(0)
spaceship.goto(0, -200)

moveShipBy = 0

while True:
    spaceship.forward(moveShipBy)
    win.update()
    time.sleep(0.02)


turtle.done()
