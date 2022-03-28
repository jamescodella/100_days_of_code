# Day 2: Tip and Bill Spliting Calculator 

print('Welcome to the tip calculator.')

total = input('What was the total bill? $')
tip_percentage = input('What percentage tip would you like to give? 10, 12, or 15? ')
num_people = input('How many people are splitting the bill? ')
total_per_person = float(total) * (1 + float(tip_percentage)/100) / float(num_people)

print(f'Each person should pay: $ {total_per_person:.2f}')
