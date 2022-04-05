import turtle

# Global vars
ALIGNMENT = 'center'
FONT = 'Helvetica'
FONT_SIZE = 20
FONT_ATTRIBUTE = 'normal'

class Score(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.sety(270)
        self.score = 0
        self.color('white')
        self.write(f'Score : {self.score}', move=False, align='center', font=(FONT, FONT_SIZE, FONT_ATTRIBUTE))
    
    def inc_score(self):
        self.score +=1 
        self.clear()
        self.write(f'Score : {self.score}', move=False, align='center', font=(FONT, FONT_SIZE, FONT_ATTRIBUTE))

    def game_over(self):
        self.sety(0)
        self.write(f'GAME OVER! :(', move=False, align='center', font=(FONT, FONT_SIZE, 'bold'))