#Example_20
import turtle
window = turtle.Screen()
window.setup(800, 600)
window.title("yuki`s example20")

t = turtle.Turtle()
t.speed("fastest")
t.pencolor("black")
t.penup()
t.hideturtle()

myAge = window.numinput("AGE INPUT", "Enter age:", 1, minval =1, maxval =120)


if myAge >=18:
    t.write("you are an adult")
else:
    t.write("you are a child") 
    
    








turtle.exitonclick()