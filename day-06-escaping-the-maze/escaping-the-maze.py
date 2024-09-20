# Day 6 Project: Escape Maze (Reeborg's World: https://reeborg.ca/index_en.html)

def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
