# Turtle Challenge 5: Generate a random walk with RGB colors

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.pensize(10)
tim.speed("fast")

angle = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for _ in range(random.randint(100, 300)): 
    tim.color(random_color())
    tim.forward(50)
    tim.setheading(random.choice(angle))
            
screen = t.Screen()
screen.exitonclick()
