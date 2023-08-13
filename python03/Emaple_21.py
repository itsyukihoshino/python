#Example_20
import turtle
window = turtle.Screen()
window.setup(800, 600)
window.title("yuki`s game")

t = turtle.Turtle()
t.speed("fastest")
t.pencolor("black")
t.penup()
t.hideturtle()

#textinput method

mycolor = window.textinput("guess color","blue or green")


# mycolor = blue => boy
# mycolor = green => girl

 

if mycolor == "blue":
    t.write("you are a boy")
elif mycolor == "green":







            
    t.write("you are a girl")









turtle.exitonclick()
# A = B give B to A
# A == B A equals B