# Import the 'turtle' library for creating graphics and 'time' for adding time delays

import turtle
import time

# Define a function 'left' to move the ship to the left
def left():                                                                                                                                                                                                                                                                                                  
    global moveShipBy
    moveShipBy = -3
    
# Define a function 'right' to move the ship to the right
def right():
    global moveShipBy
    moveShipBy = 3
    
# Define a function 'space' to shoot a bullet from the spaceship
def space():
    global bullet
    global spaceship
    
    if bullet.isvisible() == False:
        bullet.goto(spaceship.xcor(),spaceship.ycor()+45)
        bullet.showturtle()  
        
        
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
        
 
    if bullet.ycor() > (win.window_height()/2):
        bullet.hideturtle()
        
    if spaceship.xcor() > 325:
        moveShipBy = 0
    elif spaceship.xcor() < -325:
        moveShipBy = 0    
 
    win.update()
    time.sleep(0.02)  