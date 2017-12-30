import random
import turtle

snake = turtle.Turtle()


def right():
    snake.right(90)


def left():
    snake.left(90)


def forward():
    snake.forward(20)
    anim()
    body.append(save_coor())
    turtle.ontimer(forward, 300)


def save_coor():
    return (snake.pos())


def a():
    return random.randint(-30, 30) * 10

def anim():
    snake.dot(20, 'red')

# Create apple
def apple():
    snake.hideturtle()
    ap_pos = snake.position()
    snake.up()
    snake.setpos(a(), a())
    snake.dot(40, 'green')
    snake.goto(ap_pos)
    snake.showturtle()
    return ap_pos

apple_1 = apple()
apple_2 = apple()
apple_3 = apple()

snake.up()
turtle.ontimer(forward, 200)
turtle.onkey(left, 'a')
turtle.onkey(right, 'd')
turtle.listen()
turtle.mainloop()


