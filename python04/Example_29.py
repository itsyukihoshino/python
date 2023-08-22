import turtle

Win = turtle.Screen()
Win.setup(800, 600)
Win.title('Example_29 - polygon')

t1 = turtle.Turtle()
t1.speed("fast")
t1.pencolor("light green")
t1.pensize(5)

t1.fillcolor("cyan")
t1.begin_fill()
t1.goto(-120, 66)
t1.goto(88, 55)
t1.goto(43, -99)
t1.goto(-33, -55)
t1.home()
t1.end_fill()
turtle.exitonclick()