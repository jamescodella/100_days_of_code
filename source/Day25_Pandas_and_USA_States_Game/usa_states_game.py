from re import L
import turtle as t
import pandas as pd
import time


screen = t.Screen()
screen.title('USA States Game 🇺🇸')
screen.setup(height=491, width=725)
screen.bgpic('data/blank_states_img.gif')
screen.tracer(0)

state_locations = pd.read_csv('data/50_states.csv')

def game_over(score = '0 / 50'):
    message = t.Turtle()
    message.hideturtle()
    message.penup()
    message.write(f'GAME OVER', align='center', font=('Helvetica', 30, 'normal'))
    message.sety(message.ycor()-30)
    message.write(f'Your score: {score}', align='center', font=('Helvetica', 30, 'normal'))


def correct_answer(state):
    correct_state = t.Turtle()
    correct_state.hideturtle()
    correct_state.penup()
    x = state_locations[state_locations['state'] == state]['x'].values[0]
    y = state_locations[state_locations['state'] == state]['y'].values[0]
    correct_state.goto(x,y)
    correct_state.write(state, align='center', move=True, font=('Helvetica', 14, 'normal'))



def main():

    correct_answers = {}
    continue_playing = True
    num_states = len(state_locations)


    while continue_playing:
        screen.update()
        state = t.textinput(title=f'{len(correct_answers)} / {num_states} States Correct', prompt='Enter the name of a state')

        if state in state_locations['state'].values and state not in correct_answers.keys():
            correct_answers[state] = 1
            correct_answer(state)
           
        elif state not in state_locations['state'].values and state not in correct_answers.keys():
            continue_playing = False

    game_over(score = f'{len(correct_answers)} / {num_states}')

    states_to_learn = [st for st in state_locations['state'].to_list() if st not in correct_answers.keys()]
    states_to_learn = pd.DataFrame(states_to_learn, columns=['States To Learn'])
    states_to_learn.to_csv('states_to_learn.csv')
    screen.exitonclick()

if __name__ == '__main__':
    main()