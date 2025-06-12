import random
import turtle
from turtle import Turtle, Screen

screen = Screen()

is_race_on = False

screen.setup(500, 400)

colors = ["red", "orange", "green", "blue", "yellow", "purple"]

user_bet = turtle.textinput(title="Make your bet", prompt="Who will win the race? Enter a color: ")

y_position = [-70, -40, -10, 20, 50, 80]

turtles = []

for index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(-230, y=y_position[index])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(1,6)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            if turtle.pencolor() == user_bet:
                print(f"You win!, The winner is {turtle.pencolor()} turtle")
            else:
                print(f"You lose!, The winner is {turtle.pencolor()} turtle")
            is_race_on = False



screen.exitonclick()
