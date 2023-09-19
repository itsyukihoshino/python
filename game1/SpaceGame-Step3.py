import turtle

def left():
    print("left")

def right():
    print("right")
   
turtle.listen() 
turtle.onkey(left, "Left")
turtle.listen() 
turtle.onkey(right, "Right")
win = turtle.Screen()
win.title("SPACE SHIP VS WITH UFOS")
win.setup(800, 600)

win.bgpic("space-bg.gif")

#register graphic with turtle graphics
turtle.register_shape("ship.gif")

#create a turtle for my ship
spaceship = turtle.Turtle()
spaceship.shape("ship.gif")
spaceship.penup()
spaceship.speed(0)
spaceship.goto(0, -200)



