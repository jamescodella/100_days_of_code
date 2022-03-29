# Day 6: Escape Maze
# This can be used in the web app Reeborg's World: https://reeborg.ca/reeborg.html

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() == False:
    if right_is_clear():
        turn_right()
        move()
    if front_is_clear():
        move()
    else: 
        turn_left()