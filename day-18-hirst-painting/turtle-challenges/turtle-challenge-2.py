# Turtle Challenge 2: Draw a dashed line

from turtle import Turtle, Screen

tim = Turtle()

for _ in range(15):
    tim.forward(10)
    tim.up()
    tim.forward(10)
    tim.down()

screen = Screen()
screen.exitonclick()
