import turtle

window = turtle.Screen()
window.setup(800, 600)
window.title("color fun")

t = turtle.Turtle
t.speed("slowest")

colors = ("red", "blue", "green", "yellow", "black")

for color in colors:
      t.fillcolor(color)
      t.begin_fill()
      t.circle(50)
      t.end_fill()