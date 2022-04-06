import turtle

# Glboal vars
STARTING_SPACES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():
    def __init__(self, color='white'):
        self.blocks = []
        self.blocks = []
        self.color = color
        self.initailize_snake()

    def initailize_snake(self):
        for loc in STARTING_SPACES:
            self.add_block(loc)
    
    def add_block(self, pos):
        self.blocks.append(turtle.Turtle(shape='square'))
        self.blocks[-1].color(self.color)
        self.blocks[-1].penup()
        self.blocks[-1].shape()
        self.blocks[-1].goto(pos)
    
    def grow(self):
        self.add_block(self.blocks[-1].position())

    def move(self):
        for block in range(len(self.blocks)-1, 0, -1):
            self.blocks[block].goto(self.blocks[block - 1].xcor(), self.blocks[block - 1].ycor())
        self.blocks[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.blocks[0].heading() != DOWN:
            self.blocks[0].setheading(UP)
    
    def down(self):
        if self.blocks[0].heading() != UP:
            self.blocks[0].setheading(DOWN)

    def left(self):
        if self.blocks[0].heading() != RIGHT:
            self.blocks[0].setheading(LEFT)

    def right(self):
        if self.blocks[0].heading() != LEFT:
            self.blocks[0].setheading(RIGHT)

    def reset(self):
        for block in self.blocks:
            block.goto(1000,1000)
        self.blocks.clear()
        self.initailize_snake()