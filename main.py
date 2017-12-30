import random
import turtle

snake = turtle.Turtle()
snake_body = [(0, 0)]


def right():
    snake.right(90)


def left():
    snake.left(90)


def forward():
    snake.forward(20)
    anim()
    snake_body.append(save_coor())
    if save_coor() != apple:
        snake_body.pop(0)
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

apple = apple()

snake.up()
turtle.ontimer(forward, 200)
turtle.onkey(left, 'a')
turtle.onkey(right, 'd')
turtle.listen()
turtle.mainloop()


print(snake_body)