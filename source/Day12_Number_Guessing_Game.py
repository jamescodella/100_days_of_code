# Day 12: Number guessing game

import random

ascii_art = '''

 ____  _  _  ___  _  _  ____  ____  ____ 
(  _ \( \/ )/ __)/ )( \(  __)/ ___)/ ___)
 ) __/ )  /( (_ \) \/ ( ) _) \___ \\____ \\
(__)  (__/  \___/\____/(____)(____/(____/


'''

NUM_TURNS_EASY = 10
NUM_TURNS_HARD = 5

def welcome():
    '''
    Prints ascii art and a welcome message.
    '''
    print(ascii_art)
    print('Welcome to PyGuess, the number guessing game!\n')

def set_difficulty():
    '''
    Sets game difficulty level (10 or 5 attempts)
    '''
    difficulty = input('Choose a difficulty level, \'easy\' or \'hard\' ')
    if difficulty == 'easy':
        return NUM_TURNS_EASY
    else: 
        return NUM_TURNS_HARD
    
def check_guess(guess, number, num_guesses):
    '''
    Compares the player's guess with the computer's random number.
    '''
    if guess == number:
        print(f'You win! You guessed {number} which is my number!')
        return num_guesses
    elif guess > number:
        print('Your guess is too high.')
    else:
        print('Your guess is too low.')
    
    print('guess again')
    print(f'you have {num_guesses-1} guesses left.')
    return num_guesses-1

def play_pygame():
    '''
    Main game function
    '''
    welcome()
    
    number = random.randint(1,100)
    print('I\'m thinking of an integer between 1 and 100...')

    num_guesses = set_difficulty()
 
    # loop for gameplay
    while num_guesses > 0:
        guess = int(input('Make a guess: '))
        num_guesses = check_guess(guess, number, num_guesses)
        
        if guess == number:
            break

        
    if num_guesses == 0:
        print('You lost! You\'re out of guesses.')

    again = input('Would you like to play again (y) or (n)? ').lower()

    if again == 'y' or again == 'yes':
        play_pygame()

if __name__ == '__main__':
    play_pygame()