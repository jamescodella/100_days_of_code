import turtle
import random

class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('green') 
        self.speed('fastest')
        temp_x = random.randint(-280, 280)
        temp_y = random.randint(-280, 280)
        self.goto(temp_x, temp_y)

    def move(self):
        temp_x = random.randint(-280, 280)
        temp_y = random.randint(-280, 280)
        self.goto(temp_x, temp_y)

