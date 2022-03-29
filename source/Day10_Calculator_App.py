# Day 10: Calculator App

import os

ascii_art = '''
 _____________________
|  _________________  |
| |     Welcome!    | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

'''

def apply_operation(first, op, second):
    '''
    This funciton will apply the math operation on the first and second numbers in left-to-right order.
    There are a few more operations than used in the course, such as integer division (//), modulus (%), and power (**)
    '''
    if op == '+':
        return first + second
    elif op == '-':
        return first - second
    elif op == '*' or op == 'x' or op == 'X':
        return first * second
    elif op == '/':
        return first / second
    elif op == '//':
        return first // second
    elif op == '%':
        return first % second
    elif op == '**' or op == '^':
        return first ** second
    else:
        raise IOError('The operation you entered isn\'t supported by this app.')

def calculator():

    # Print welcome art
    print(ascii_art)

    # Initialize variables
    calculate = True
    first_number = None 

    # Loop until no more calculations are desired.
    while calculate:
        if first_number is None:
            first_number = input('What\'s the first number? ')
        op = input('Pick an operation (+, -, *, /, //, %, **): ')
        second_number = input('What\'s the second number? ')

        result = str(apply_operation(float(first_number), op, float(second_number)))
        print(first_number + ' ' + op + ' ' + second_number + ' = ' + result + '\n')

        continue_option = input(f'Type \'y\' to continue calculating with {result}, \'n\' to start a new calculation, or \'exit\' to quit the app: ').lower()
        
        if continue_option == 'n':
            first_number = None
            os.system('cls' if 'Win' in os.name else 'clear')

        elif continue_option == 'y':
            first_number = result
        elif continue_option == 'exit':
            break

# Run the function
if __name__ == '__main__':
    calculator()