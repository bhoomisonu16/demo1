import turtle
p=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("palegreen")
p.pensize(5)
p.pencolor("gold")
p.speed(0)
p.hideturtle()

p.begin_fill()
p.fillcolor("red")

for i in range(12):
    p.forward(40)
    p.left(90)
    p.backward(80)
    p.right(70)
    p.forward(40)
    p.left(90)
    p.forward(80)
    p.right(20)
    p.forward(40)

p.end_fill()
