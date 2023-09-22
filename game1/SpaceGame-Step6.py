import turtle
import time

def left():                                                                                                                                                                                                                                                                                                  
    global moveShipBy
    moveShipBy = -3
    
def right():
    global moveShipBy
    moveShipBy = 3
    
def space():
    global bullet
    global spaceship
    
    if bullet.isvisibl() == False:
        bullet.goto(spaceship.xcor(),spaceship.ycor)
        bullet.showturtle   
        
        
#enable and register keyboard events
turtle.listen()
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(space, "space")

win = turtle.Screen()
win.title("SPACE SHIP Vs UFOS!")
win.setup(800, 600)
win.bgpic("space-bg.gif")
win.tracer(0)

#register graphic with turtle graphics
turtle.register_shape("ship.gif")
turtle.register_shape("bullet.gif")

#create a turtle for my ship
spaceship = turtle.Turtle()
spaceship.shape("ship.gif")
spaceship.penup()
spaceship.speed(0)
spaceship.goto(0, -200)

#create a turtle for my bullet laser blast
bullet = turtle.Turtle()
bullet.hideturtle
bullet.shape("bullet.gif")
bullet.penup()
moveShipBy = 0
#game loop that redraws our screen each time the loop executes
while True:
    
    spaceship.forward(moveShipBy)

    if bullet.isvisible():
        bullet.setheading(90)
        bullet.forward(25)

    if bullet.ycor() > 200:
        bullet.hideturtle()

    if spaceship.xcor() > 325:
        moveShipBy = 0
    elif spaceship.xcor() < -325:
        moveShipBy = 0 