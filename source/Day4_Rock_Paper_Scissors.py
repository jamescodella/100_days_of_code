# Day 4: Rock Paper Scissors Game

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choices = [rock, paper, scissors]

your_choice = input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n')
print(your_choice)
if your_choice == '':
    your_choice = random.randint(0,2)
    print('No choice entered. Will choose randomly for you.')
elif your_choice not in [0,1,2]:
    print('Invalid choice!')
    quit()

your_choice = int(your_choice)

computers_choice = random.randint(0,2)

print('\nYou chose: \n' + choices[your_choice])
print('\nComputer chose: \n' + choices[computers_choice]+'\n')

if your_choice == computers_choice:
    print('It\'s a tie!')
elif your_choice == 0:
    if computers_choice == 1:
        print('You lose!')
    if computers_choice == 2:
        print('You win!')
elif your_choice == 1:
    if computers_choice == 2:
        print('You lose!')
    if computers_choice == 0:
        print('You win!')
elif your_choice == 2:
    if computers_choice == 0:
        print('You lose!')
    if computers_choice == 1:
        print('You win!')