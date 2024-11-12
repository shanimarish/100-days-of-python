# Turtle Challenge 4: Generate a random walk

from turtle import Turtle, Screen
import random

tim = Turtle()
colors = ["cornflower blue", "light sky blue", "teal", "sandy brown", "peach puff", "light salmon", "gold", "medium purple", "light pink"]
angle = [0, 90, 180, 270]

tim.pensize(10)
tim.speed("fast")

for _ in range(random.randint(100, 300)): 
    tim.color(random.choice(colors))
    tim.forward(50)
    tim.setheading(random.choice(angle))
            
screen = Screen()
screen.exitonclick()
