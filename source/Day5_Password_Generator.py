# Day 5: Password Generator

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# My code implementation of the "Hard Level" is below:

password_chars = []

for i in range(nr_letters):
    l = random.randint(0,len(letters)-1)
    password_chars.append(letters[l])

for i in range(nr_symbols):
    l = random.randint(0,len(symbols)-1)
    password_chars.append(symbols[l])

for i in range(nr_numbers):
    l = random.randint(0,len(numbers)-1)
    password_chars.append(numbers[l])

randomized_password = ''

while password_chars != []:
    random_index = random.randint(0,len(password_chars)-1)
    randomized_password += password_chars[random_index]
    password_chars.remove(password_chars[random_index])

print(randomized_password)