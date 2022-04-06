# Day 23: Crossy Turtle game
# Modifications from course:
# - Cars travel right->left AND left->right
# - Turtle can move up, left, and right
# - Spacebar gives Turtle a speed boost


import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('Crossy Turtle 🐢 🛣 ')

# Initialize objects
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

# Listen for key events
screen.listen()
screen.onkeypress(fun=player.move_up, key='Up')
screen.onkeypress(fun=player.move_left, key='Left')
screen.onkeypress(fun=player.move_right, key='Right')
screen.onkeypress(fun=player.move_up_fast, key='space')


game_is_on = True

# Main game loop
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.move()

    # reach end and advance to next level
    if player.ycor() > 250:
        player.level_up()
        scoreboard.level_up()
        cars.increase_speed()

    # Logic for the turtle getting hit by a car
    for c in cars.cars:
        if player.distance(c) < 22:
            game_is_on = False

scoreboard.game_over()

screen.exitonclick()