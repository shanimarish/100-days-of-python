# Turtle Challenge 3: Drawing different shapes

from turtle import Turtle, Screen
import random

tim = Turtle()
colors = ["powder blue", "sky blue", "cornflower blue", "royal blue", "blue", "medium blue", "navy", "dark blue", "midnight blue", "deep sky blue", "dodger blue"]

def draw_shape(shape_sides):
    angle = 360 / shape_sides
    for _ in range(shape_sides): 
        tim.forward(100)
        tim.right(angle)

for shape_sides_num in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_sides_num)
    

screen = Screen()
screen.exitonclick()
