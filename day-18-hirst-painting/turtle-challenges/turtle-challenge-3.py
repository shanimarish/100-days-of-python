# Turtle Challenge 3: Drawing different shapes

from turtle import Turtle, Screen

tim = Turtle()

for sides in range(3, 10):  
    angle = 360 / sides
    for _ in range(sides): 
        tim.forward(100)
        tim.right(angle)

screen = Screen()
screen.exitonclick()
