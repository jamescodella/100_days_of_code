import turtle as t
import random

STEP_SIZE = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Ball(t.Turtle):

    def __init__(self, color='white'):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color(color)
        self.x_step = 10
        self.y_step = 10
        self.move_speed = 0.1
    
    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def v_bounce(self):
        self.y_step = -self.y_step
    
    def h_bounce(self):
        self.x_step = -self.x_step
        self.move_speed *= 0.9


    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.1
        dir = random.randint(0,1)
        if dir == 0:
            self.x_step = -self.x_step
        dir = random.randint(0,1)
        if dir == 0:
            self.y_step = -self.y_step
    