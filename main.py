import random
import turtle

snake = turtle.Turtle()


def right():
    snake.right(90)


def left():
    snake.left(90)


def forward():
    snake.forward(5)
    turtle.ontimer(forward, 200)

def a():
    return random.randint(-300, 300)

# Create apple
x, y = snake.position()
snake.up()
snake.setpos(a(), a())
snake.dot(15, 'green')
snake.goto(x, y)

snake.up()
turtle.ontimer(forward, 200)
turtle.onkey(left, 'a')
turtle.onkey(right, 'd')
turtle.listen()
turtle.mainloop()


