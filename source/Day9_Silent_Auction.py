# Day 9: Silent Auction

import os

def find_max_value_in_dict(d):
    '''
    A simple helper funciton to find the key with the max value in a dictionary
    '''
    max_value = float('-inf')
    max_key = None
    for key, val in d.items():
        if val > max_value:
            max_value = val
            max_key = key

    return key

# Gavel art from https://ascii.co.uk/art/gavel
gavel_art = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\

'''

def silect_auction():
    add_bidders = True
    bids = {}

    # Welcome message
    print('\n\n                 Welcome to the Silent Auction!')
    print(gavel_art + '\n\n')

    # Collect names and bids
    while True:
        name = input("What is your name?: ")
        bid = float(input('How much would you like to bid (in $)?: '))
        bids[name] = bid

        add_bidders = input('Are there more bidders to add? Type yes or no: ').lower()
        if add_bidders == 'no':
            break
        # else continue adding bidders
        os.system('cls' if 'Win' in os.name else 'clear')

    # Find winner with max bid
    winner = max(bids, key=bids.get) # Pythonic way
    #winner = find_max_value_in_dict(bids) # Alternate way: iterating over dictionary items

    print(f'*** The winner is {winner} with a bid of: ${round(bids[winner])}! ***')

if __name__ == '__main__':
    silect_auction()