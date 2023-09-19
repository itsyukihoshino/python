import turtle

win = turtle.Screen()
win.title("SPACE SHIP VS WITH UFOS")
win.setup(800, 600)

win.bgpic("space-bg.gif")

#register graphic with turtle graphics
turtle.register_("ship.gif")

#create a turtle for my ship
spaceship = turtle.Turtle()
spaceship.shape("ship.gif")

