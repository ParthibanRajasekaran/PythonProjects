from turtle import Screen
import random
import turtle as t

timmy = t.Turtle()
timmy.shape("turtle")
t.colormode(255)

# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)

# color_list = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

#
# for _ in range(15):
#     timmy.pendown()
#     timmy.color(random.choice(color_list))
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

# color_list = ["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"]
#
# for n in range(4,10):
#     angle = 360/n
#     timmy.color(random.choice(color_list))
#     for _ in range(n):
#         timmy.forward(100)
#         timmy.right(angle)

def draw_spirograph(timmy, rotate):
    for _ in range(int(360/rotate)):
        timmy.right(rotate)
        draw_circle(timmy, 100)

def draw_circle(timmy, radius):
    timmy.color(random_color())
    timmy.circle(radius)

def randomDirectionForward(timmy, steps):
    direction = [0,90,180,270]
    timmy.pensize(10)
    for _ in range(steps):
        timmy.speed('fastest')
        timmy.color(random_color())
        timmy.setheading(random.choice(direction))
        timmy.forward(20)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def randomwalk1D(timmy , n):
    x, y = 0, 0
    path = [(x, y)]

    # Boundaries
    min_bound = -1000
    max_bound = 1000
    for _ in range(n):
        direction = random.choice(['up', 'down', 'left', 'right'])

        if direction == 'up' and y < max_bound:
            y += 20
        elif direction == 'down' and y > min_bound:
            y -= 20
        elif direction == 'left' and x > min_bound:
            x -= 20
        elif direction == 'right' and x < max_bound:
            x += 20

        path.append((x, y))

    timmy.speed('fastest')
    timmy.penup()
    timmy.setpos(path[0])
    for position in path[1:]:
        timmy.color(random_color())
        timmy.pensize(10)
        timmy.pendown()
        print(position)
        timmy.setpos(position)



# randomwalk1D(timmy, 100)
#
randomDirectionForward(timmy, 500)

# draw_circle(timmy, 100)

# draw_spirograph(timmy, 36)

screen = Screen()


screen.exitonclick()
