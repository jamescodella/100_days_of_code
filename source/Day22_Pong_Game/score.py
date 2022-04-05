import turtle as t

FONT = ('Mono', 30, 'normal')
ALIGNMENT = 'center'

class Score(t.Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.scores = {'p1' : 0,
                     'p2' : 0}
        self.penup()
        self.sety(260)
        self.color('white')
        self.write(f'{self.scores["p1"]}    {self.scores["p2"]}', align=ALIGNMENT, font=FONT)
    
    def inc_score(self, player):
        self.scores[player] += 1
        self.clear()
        self.write(f'{self.scores["p1"]} : {self.scores["p2"]}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.write(f'GAME OVER :(', align=ALIGNMENT, font=FONT)

