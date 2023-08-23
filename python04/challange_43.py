import turtle

win = turtle.Screen()
win.setup(800, 600)
win.title('challenge 23 - Draw your Own Emoji')

t1 = turtle.Turtle()
t1.speed("fast")
t1.pencolor("yellow")
t1.pensize(3)

t1.penup()
t1.goto(0, -150)

t1.pendown()
t1.fillcolor("yellow")
t1.begin_fill()
t1.circle(202)
t1.end_fill()

t1.goto(-60, -20)
t1.fillcolor("white")
t1.begin_fill()
t1.circle(50)
t1.end_fill()

t1.goto(60, -20)
t1.fillcolor("white")
t1.begin_fill()
t1.circle(50)
t1.end_fill()

t1.penup()
t1.pencolor("black")
t1.fillcolor("black")
t1.goto(-70, 0)
t1.pendown()
t1.begin_fill()
t1.circle(15)
t1.end_fill()
turtle.exitonclick()