import turtle

turtle.speed(99)

#create and setup turtle window
win = turtle.Screen()
win.setup(800,600)
# win.bgpic('grid.gif')
win.title('Example 20 ')

#create turtle object
t1 = turtle.Turtle()

t1.speed("slowest")
t1.pencolor("blue")
t1.pensize(5)

#draw turtle
t1.penup()
t1.goto(100,100)
t1.pendown()
t1.goto(-100,100)
t1.goto(-100,-100)
t1.goto(100,-100)
t1.goto(100,100)
t1.circle(50)
t1.right(180)
t1.penup()
t1.forward(200)
t1.pendown()
t1.right(90)
t1.circle(50)
t1.left(180)
t1.forward(50)
t1.left(90)
t1.penup()
t1.forward(66)
t1.left(90)
t1.pendown()
t1.circle(15)
t1.right(90)
t1.penup()
t1.forward(50)
t1.pendown()
t1.circle(15)
turtle.bgcolor("light green")
t1.right(90)
t1.penup()
t1.forward(100)
t1.pendown()















win.exitonclick()