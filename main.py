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

def a():
    return random.randint(-300, 300)

# Create apple
x, y = t.position()
t.up()
t.setpos(a(), a())
t.dot(10, 'green')
t.goto(x, y)

move.up()
turtle.ontimer(forward, 200)
turtle.onkey(left, 'a')
turtle.onkey(right, 'd')
turtle.listen()
turtle.mainloop()


