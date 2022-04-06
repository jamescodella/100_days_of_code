# Day 24: Mail Merge Challenge
# Boilerplate comment below

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names_list = []
with open('Input/Names/invited_names.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip() # line.replace('\n', '')
        names_list.append(line)
        
with open('Input/Letters/starting_letter.txt', 'r') as file:
    letter = file.read()

custom_letters = {}
for name in names_list:
    custom_letter = letter.replace('[name]', name)
    custom_letters[name] = custom_letter

for name, letter in custom_letters.items():
    with open('Output/ReadyToSend/letter_for_' + name + '.txt', 'w+') as file:
        file.write(letter)