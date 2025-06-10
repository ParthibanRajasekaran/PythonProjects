import random
import turtle as t
from turtle import Screen

timmy = t.Turtle()
# timmy.shape("turtle")

import colorgram

# Extract 6 colors from an image.

def get_color_list():
    colors = colorgram.extract('hirst-image.jpg', 45)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors.append((r,g,b))
    return rgb_colors

color_list = [(249, 248, 248), (233, 241, 239), (226, 233, 239), (1, 9, 30), (242, 234, 240), (122, 95, 42), (71, 32, 22), (238, 212, 72), (220, 81, 60), (226, 117, 101), (93, 1, 20), (178, 140, 171), (150, 92, 116), (34, 90, 26), (8, 154, 72), (205, 63, 91), (168, 129, 78), (2, 64, 146), (5, 220, 218), (220, 178, 218), (3, 78, 28), (81, 134, 179), (127, 155, 177), (81, 109, 133), (115, 188, 167), (14, 213, 220), (228, 174, 166), (133, 224, 211), (114, 22, 38), (189, 190, 197), (243, 205, 9), (71, 67, 48), (90, 50, 44), (118, 226, 230), (61, 65, 66)]

# def random_color():
#     return random.sample(color_list, 10)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def walk_forward():
    timmy.penup()
    timmy.goto( -200, 0)
    timmy.pendown()
    timmy.pensize(10)
    timmy.speed('fastest')
    t.colormode(255)
    for i in range(10):
        timmy.left(360)
        for _ in range(10):
            timmy.dot(20, random.choice(color_list))
            timmy.penup()
            timmy.forward(40)
            timmy.pendown()
        timmy.penup()
        timmy.goto(-200, 40 + 40 * i)


screen = Screen()
screen.colormode(255)
walk_forward()

screen.exitonclick()
