# Day 20 Project: Turtle Race

from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_direction = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.up()
    new_turtle.goto(x=-230, y=y_direction[index])
    all_turtles.append(new_turtle)

if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
