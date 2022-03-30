# Day 14: Higher or Lower Game

from game_data import data
from art import logo, vs
import random
import os

def pick_random_person(): 
    '''
    This returns a random choice from a list.
    '''
    return random.choice(data)

def check_answer(A, B, guess):
    '''
    Checks a players answer, compares relation between A and B, and returns True is guess is correct, false otherwise.
    '''
    if guess == 'a':
        if A['follower_count'] > B['follower_count']:
            return True
        else: 
            return False

    elif guess == 'b':
        if B['follower_count'] > A['follower_count']:
            return True
        else: 
            return False

def new_question(A, B):
    '''
    This function presents a question to the user, takes their guess, and returns it to the caller.
    '''
    print('Compare ' + A['name'] + ', a ' + A['description'] + ', from ' + A['country'] + '.')
    print(vs)
    print('Compare ' + B['name'] + ', a ' + B['description'] + ', from ' + B['country'] + '.')
    return input('Who has more followers? Type \'A\' or \'B\' ').lower()
    
def run_game():
    '''
    The main function for Higher or Lower gameplay.
    '''

    # Initialize vars
    guessed_correctly = True
    A = {}
    B = {}
    score = 0

    while guessed_correctly:
        print(logo)
        if score > 0:
            print(f'You\'re right! Current score: {score}')
        
        A = pick_random_person()
        B = A
        while A == B: # Ensures person B will be different than person A
            B = pick_random_person()
        
        guess = new_question(A, B)

        if guess in ['quit', 'exit']: # adding feature where the player can exit the game at any time.
            quit()

        guessed_correctly = check_answer(A, B, guess)
        if guessed_correctly == True:
            score += 1

        os.system('cls' if 'Win' in os.name else 'clear')


    # End of game summary
    print(logo)
    print(f'Sorry, that\'s wrong. Final score: {score}')

if __name__ == '__main__':
    run_game()