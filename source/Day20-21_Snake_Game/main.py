# Day 20 & 21: Snake game

from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score


screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Python Snake Game')
screen.tracer(0)

# Initialize segements
snake = Snake()
food = Food()
score = Score()

game_running = True

# Listen for keypresses
screen.listen()
screen.onkey(fun=snake.up, key = 'Up')
screen.onkey(fun=snake.down, key = 'Down')
screen.onkey(fun=snake.left, key = 'Left')
screen.onkey(fun=snake.right, key = 'Right')

while game_running:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision w/ food
    if snake.blocks[0].distance(food) < 15:
        snake.grow()
        food.move()
        score.inc_score()

    # Detect collision w/ wall
    if snake.blocks[0].xcor() > 280 or snake.blocks[0].ycor() > 280 or snake.blocks[0].xcor() < -280 or snake.blocks[0].ycor() < -280:
        game_running = False

    # Detect collision with tail
    for b in snake.blocks[1:]: # avoid comparing head with head
        if snake.blocks[0].distance(b) < 10:
            game_running = False
            
score.game_over()
    
screen.exitonclick()