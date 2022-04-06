import turtle as t

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(t.Turtle):

    def __init__(self):
        super().__init__(shape='turtle')
        self.color('green')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    pass

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_up_fast(self):
        self.forward(MOVE_DISTANCE*2)

    def move_left(self):
        if self.xcor() > -250:
            self.setx(self.xcor() - MOVE_DISTANCE)
        
    def move_right(self):
        if self.xcor() < 250:
            self.setx(self.xcor() + MOVE_DISTANCE)

    def level_up(self):
        self.goto(STARTING_POSITION)

