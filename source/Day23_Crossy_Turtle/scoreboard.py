import turtle as t
FONT = ("Courier", 24, "normal")


class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-270, 270)
        self.write(f'Level: {self.level}', align='left', font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f'Level: {self.level}', align='left', font=FONT)

    def game_over(self):
        self.goto(0,0) 
        self.write(f'GAME OVER :(', align='center', font=FONT)