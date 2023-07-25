import turtle
# adjust pen size
turtle.pensize(3)
turtle.shape("turtle")

#outer
turtle.penup()
turtle.goto(325,0)
turtle.left(90)  
turtle.pendown()
turtle.color("red")

turtle.begin_fill()
turtle.circle(325)
turtle.end_fill()

turtle.right(90)


#paint circle
turtle.penup()
turtle.goto(175,0)
turtle.left(90)
turtle.pendown()
turtle.color("blue")

turtle.begin_fill()
turtle.circle(175)
turtle.end_fill()


#star
turtle.color("white")
turtle.begin_fill()
turtle.penup()
turtle.goto(-166,54)
turtle.right(90)
turtle.pendown()
turtle.forward(333)
turtle.right(144)
turtle.forward(333)
turtle.right(144)
turtle.forward(333)
turtle.right(144)
turtle.forward(333)
turtle.right(144)
turtle.forward(333)
turtle.right(144)

turtle.end_fill()


