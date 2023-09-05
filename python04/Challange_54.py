import turtle

window = turtle.Screen()
window.setup(800, 600)
window.title('Challenge 18')

t = turtle.Turtle()
t.speed("fastest")
t.pencolor("blue")
t.penup()
t.hideturtle()

emotion = window.textinput("EMOTION INPUT","Enter and emotion(happy, sad, or angry):")

if emotion == None:
    t.fillcolor("black")
    t.begin_fill()
    t.circle(100)
    t.end_fill()
elif emotion == "sad":
    t.fillcolor("blue")  
    t.begin_fill()
    t.circle(100)
    t.end_fill()
elif emotion == "happy":
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(100)
    t.end_fill()