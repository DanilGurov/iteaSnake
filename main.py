import random
import turtle

move = turtle.Turtle()

def right():
    move.right(90)

def left():
    move.left(90)

def forward():
    move.forward(10)
    turtle.ontimer(forward, 200)


move.up()
turtle.ontimer(forward, 200)
turtle.onkey(left, 'a')
turtle.onkey(right, 'd')
turtle.listen()
turtle.mainloop()