from turtle import Turtle, Screen
timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(50)

def move_backward():
    timmy.backward(50)

def turn_clockwise():
    timmy.right(30)

def turn_counterclockwise():
    timmy.left(30)

def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='d', fun=turn_clockwise)
screen.onkey(key='a', fun=turn_counterclockwise)
screen.onkey(key='c', fun=clear_screen)
screen.exitonclick()