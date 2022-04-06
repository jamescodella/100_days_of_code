import turtle
import os

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
        self.read_score()
        self.color('white')
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_ATTRIBUTE))
    
    def inc_score(self):
        self.score +=1 
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_ATTRIBUTE))

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_ATTRIBUTE))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.write_score()
        self.score = 0
        self.update_scoreboard()

    def read_score(self):
        if os.path.exists('high_scores.txt'):
            with open('high_scores.txt', 'r+') as file:
                self.high_score = int(file.readlines()[-1])
        else:
            self.high_score = 0
    
    def write_score(self):
        with open('high_scores.txt', 'a+') as file:
            file.write(f'\n{self.high_score}')
            

