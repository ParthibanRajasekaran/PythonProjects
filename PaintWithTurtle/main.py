from turtle import Turtle, Screen

timmy = Turtle()
print(timmy.width())
timmy.shape("turtle")
timmy.color("blue","red")
timmy.forward(100)
timmy.left(90)
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()