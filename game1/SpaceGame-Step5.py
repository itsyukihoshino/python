import turtle
import time

def left():                                                                                                                                                                                                                                                                                                  
    global moveShipBy
    moveShipBy = -3
    
def right():
    global moveShipBy
    moveShipBy = 3  
    
#enable and register keyboard events
turtle.listen()
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")

win = turtle.Screen()
win.title("SPACE SHIP Vs UFOS!")
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

moveShipBy = 0

#game loop that redraws our screen each time the loop executes
while True:
    
    spaceship.forward(moveShipBy)
    

    if spaceship.ycor() > 325:
        moveShipBy = 0
    elif spaceship.ycor() < -325:
        moveShipBy = 0
        
    win.update()    
    time.sleep(0.02)