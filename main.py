import math
import random

import colorgram
import turtle

color_img = 'color-damient-hirst.jpg'
color = colorgram.extract(color_img, 20)


def get_color(colors):
    color_list = []
    for i in range(len(colors)):
        r = colors[i].rgb.r
        g = colors[i].rgb.g
        b = colors[i].rgb.b

        color_list.append((r, g, b))
    return color_list


color = get_color(color)

turtle.colormode(255)

timmy = turtle.Turtle()
timmy.penup()
timmy.hideturtle()
timmy.speed("fastest")
timmy.setposition(-200, -200)


def draw_dotted_art(distance, diameter, no_of_row, no_of_col):
    for _ in range(no_of_row):
        for _ in range(no_of_col):
            timmy.dot(diameter, random.choice(color))
            timmy.setx(timmy.xcor() + distance)
        timmy.setx(timmy.xcor() - distance * 10)
        timmy.sety(timmy.ycor() + distance)


draw_dotted_art(50, 20, 10, 10)

screen = turtle.Screen()
screen.exitonclick()
