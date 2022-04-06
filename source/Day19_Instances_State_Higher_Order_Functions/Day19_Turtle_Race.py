# Day 19: Turtle Race

from turtle import Turtle, Screen, color
import random

from torch import rand

if __name__ == '__main__':

    is_race_on = False
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title='Enter your bet', prompt='Enter the color of the turtle you think will win the race: ')
    print(f'Ok! You bet on {user_bet}.')
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

    turtles = []

    for idx, c in enumerate(colors):
        turtles.append(Turtle(shape='turtle'))
        turtles[idx].color(c)
        turtles[idx].penup()
        turtles[idx].goto(x=-230, y=-100+30*idx)

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in turtles:
            rand_step = random.randint(0,10)
            turtle.forward(rand_step)
            if turtle.xcor() > 230:
                winning_turtle = turtle.pencolor()
                if winning_turtle == user_bet:
                    print(f'Congratulations, you win the bet! The {winning_turtle} turtle won the race! 🐢')
                else:
                    print(f'Too bad, you lost the bet! The {winning_turtle} turtle won the race. 🐢')
                is_race_on = False        
                break

    screen.exitonclick()