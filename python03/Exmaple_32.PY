#Example_32
import turtle
window = turtle.Screen()
window.setup(800, 600)
window.title("yuki`s example20")

t = turtle.Turtle()
t.speed("fastest")
t.penup()

# window.numinput
# window.textinput

# B = window.textinput("color game","orange yellow")
# mycolor = B

mycolor  =  window.textinput("color game","orange or yellow or red")

if mycolor == "orange":
    turtle.write("you are a boy")
elif mycolor == "yellow":
    turtle.write("you are a girl")
elif mycolor == "red":
    turtle.write("you are a clown")
t.circle(90)

turtle.exitonclick()


