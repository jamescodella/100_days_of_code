import turtle as t

STEP_SIZE = 30

class Paddle(t.Turtle):

    def __init__(self, name, color='white'):
        super().__init__(shape='square')
        self.penup()
        self.color(color)
        self.setheading(-90)
        self.shapesize(stretch_len=5)
        self.name = name
        self.create_paddle()

    def create_paddle(self):
        if self.name == 'p1':
            self.setx(-370)
        else:
            self.setx(370)

    def up(self):
        if self.ycor() < 260:
            self.sety(self.ycor() + STEP_SIZE)

    def down(self):
        if self.ycor() > -260:
            self.sety(self.ycor() - STEP_SIZE)