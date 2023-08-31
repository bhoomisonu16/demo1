#Write a python program to construct a chess board
import turtle
p=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("palegreen")
p.pensize(5)
p.pencolor("black")
p.speed(0)
p.shape("turtle")
p.goto(-40, -40)

def circle():
    for i in range(4):
        p.forward(40)
        p.right(35)
    p.forward(40)

for i in range(8):
    p.penup()
    p.goto(0, 225*i)
    p.pendown()
    for x in range(8):
        if (x+i)%2 == 0:
            color = "orange"
        else:
            color = "blue"

        p.fillcolor(color)
        p.begin_fill()
        circle()
        p.end_fill()

