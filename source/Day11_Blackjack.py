# Day 11: Blackjack Capstone Project

import random
import os

# List of cards provided in the course.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Helper functions
def welcome():
    ''''
    This funciton simply prints some ascii art and a welcome message.
    '''
    ascii_art = '''
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
            |  \/ K|                            _/ |                
            `------'                           |__/           
'''

    print('\n*** Welcome to Blackjack! ***')
    print(ascii_art)


def calculate_score(hand):
    '''
    This function calculates the sum of values in a given hand.
    '''
    score = 0
    ace_indices = []
    for idx, card in enumerate(hand):
        score += card
        if card == 11:
            ace_indices.append(idx)

    for idx in ace_indices:
        if (score > 21):
            score -= 10 # One ace is now treated as a 1. 

    return score

def draw_card():
    '''
    This function randomly selects a card from the cards dict
    '''
    return random.choice(cards)

def compare_scores(players_score, dealers_score):
    '''
    This function compares dealers score with the players score to see who won the game.
    '''
    if players_score > 21:
        return 'You lose! Your hand went over 21 :('

    if dealers_score > 21:
        return 'You win! The dealer\'s hand went over 21 :)'

    elif dealers_score < players_score:
        return 'You win! :)'

    elif dealers_score ==  players_score:
        return 'It\'s a draw! :|'
    else:
        return 'You lose! :('
    
def game_summary(players_hand, players_score, dealers_hand, dealers_score):
    '''
    Summarizes final state and score of the game
    '''
    print('\n\nEND GAME SUMMARY')
    print('-------------------------')
    print(compare_scores(players_score, dealers_score))
    print('Your final hand: ' + str(players_hand) + ', your final score: ' + str(players_score))
    print('Dealer\'s final hand: ' + str(dealers_hand) +', dealer\'s final score: ' + str(dealers_score))
    print('-------------------------\n')
    

def play_blackjack():
    '''
    Main function for game play
    '''
    # Print ascii art and welcome message
    welcome()

    # Initialize hands and vars
    players_hand = []
    dealers_hand = []
    players_score = 0
    dealers_score = 0
    hit_or_stay = 'h'
    blackjack = False

    # Draw first two cards for each player
    players_hand.append(draw_card())
    players_hand.append(draw_card())
    dealers_hand.append(draw_card())
    dealers_hand.append(draw_card())

    players_score = calculate_score(players_hand)
    dealers_score = calculate_score(dealers_hand)

    print('Your hand: ' + str(players_hand) + ', your score: ' + str(players_score))
    print('Dealer\'s hand: ['+ str(dealers_hand[0]) +', _], dealer\'s score: ' + str(dealers_score))

    if players_score == 21 or dealers_score == 21: # if blackjack occurs for either player, instant win and the game stops
        print('\n***Blackjack!***')
        hit_or_stay = 's'
        blackjack = True

    while (hit_or_stay == 'h' or hit_or_stay == 'hit') and blackjack is False:
        hit_or_stay = input('Would you like to hit (h) or stay (s)? ').lower()
        if hit_or_stay == 's' or hit_or_stay == 'stay':
            print(players_hand, players_score)
            break
        
        players_hand.append(draw_card())
        print('Your hand: ' + str(players_hand) + ', your score: ' + str(players_score))
        players_score = calculate_score(players_hand)

        if players_score > 21: # Bust
            break
    
    if players_score <= 21 and blackjack is False:
        while dealers_score < 17:
            dealers_hand.append(draw_card())
            dealers_score = calculate_score(dealers_hand)

    game_summary(players_hand, players_score, dealers_hand, dealers_score)
    keep_playing = input('Play again (y) or (n)? ')
    if keep_playing == 'y' or keep_playing == 'yes':
        os.system('cls' if 'Win' in os.name else 'clear')
        play_blackjack()
    else:
        quit()

if __name__ == '__main__':
    play_blackjack()