# Day 7: Hangman Game

def draw_hangman(incorrect_guesses):
    '''
    This function draws hangman depending on then number of incorrect guesses.
    The ASCII art is included in the starter code, but I chose to 
    implement this myself for extra practice.
    '''
    print('\n====')
    if incorrect_guesses > 0:
        print('  -|')

    if incorrect_guesses > 1:
        print('   O')

    if incorrect_guesses == 2:
        print('   |')

    if incorrect_guesses == 3:
        print('  /|')    
    
    if incorrect_guesses >= 4:
        print('  /|\\')

    if incorrect_guesses == 5:
        print('  /')    
    
    if incorrect_guesses >= 6:
        print('  / \\')

    print('\n')
import random

word_list = ['test', 'this', 'out']
number_of_tries = 6
incorrect_guesses = 0

# Sample word at random
word = random.choice(word_list)

# Generate blanks 
guessed_word = ['_' for i in range(len(word))]

# Ask the user to guess the word until winning or failure.
while incorrect_guesses < number_of_tries:
    draw_hangman(incorrect_guesses)
    print('Word to guess: ', ' '.join(guessed_word))
    guess = input('Enter guess: ').lower()

    if guess not in word:
        print(f'Wrong. Your guess \'{guess}\' is not in the word.')
        incorrect_guesses += 1
    else:
        for i, w in enumerate(word):
            if w == guess:
                guessed_word[i] = w

    if '_' not in guessed_word: # No longer any more blanks
        print('You win! :)')
        quit()

# The player has lost. 
draw_hangman(incorrect_guesses)
print('You lose! :(')
