# Day 22: Pong game
import turtle as t
from venv import create
from paddle import Paddle
from ball import Ball
from score import Score
import time

# Screen setup
screen = t.Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PyPong Game')
screen.tracer(0)

def create_line(color='white'):
    '''
    Simple function to create the dashed line.
    '''
    line = t.Turtle()
    line.hideturtle()
    line.penup()
    line.color(color)
    line.goto(0,300)
    line.setheading(270)
    line.width(3)
    for i in range(40):
        line.pendown()
        line.forward(10)
        line.penup()
        line.forward(10)

def play_game():
    # Initialize objects
    game_continues = True
    player1 = Paddle('p1')
    player2 = Paddle('p2')
    score = Score()
    ball = Ball()
    create_line()

    # Key listener
    screen.listen()
    screen.onkey(fun=player1.up, key='w')
    screen.onkey(fun=player1.down, key='s')
    screen.onkey(fun=player2.up, key='Up')
    screen.onkey(fun=player2.down, key='Down')

    # Main game loop
    while game_continues:
        screen.update()
        time.sleep(ball.move_speed)

        # Ball bouncing off paddles
        if (player1.distance(ball) < 50 and ball.xcor() < -340) or (player2.distance(ball) < 50 and ball.xcor() > 340):
            ball.h_bounce()
        
        # Ball bouncing off sidewalls
        if ball.ycor() > 270 or ball.ycor() < -270:
            ball.v_bounce()
        
        # Score bouncing off paddles
        if ball.xcor() > 380:
            score.inc_score('p1')
            ball.reset()
        elif ball.xcor() < -380:
            score.inc_score('p2')
            ball.reset()

        ball.move()

    screen.exitonclick()

if __name__ == '__main__':
    play_game()