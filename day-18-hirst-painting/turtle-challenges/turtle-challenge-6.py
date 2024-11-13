# Day 6 Challenge: Draw a spirograph

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
t.bgcolor("black")
tim.pensize(2)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)

draw_spirograph(10)

screen = t.Screen()
screen.exitonclick()
