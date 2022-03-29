# Day 8: Ceaser Cipher 

def encode(text, shift_number):
    '''
    This function encodes the text by shifting right by the specified number
    '''
    shifted_text = list(text)
    for i, char in enumerate(text):

        if char.isalpha(): # Only encrypt alphabetic characters
            shifted_text[i] = chr((ord(char) + shift_number % 26))
    
    return ''.join(shifted_text)

def decode(text, shift_number):
    '''
    This function decodes the text by shifting left by the specified number
    '''
    shifted_text = list(text)
    for i, char in enumerate(text):
        if char.isalpha(): # Only decrypt alphabetic characters 
            shifted_text[i] = chr((ord(char) - shift_number % 26))
    
    return ''.join(shifted_text)

if __name__ == '__main__':

    while True:
        mode = input('Type \'encode\' to encrypt a message, or \'decode\' to decrypt a message: ').lower()
        text = input(f'Enter text to {mode}: ').lower()
        shift_number = int(input('Enter shift number: '))

        if mode == 'encode':
            print('Your encoded message is:', encode(text, shift_number))
        elif mode == 'decode':
            print('Your decoded message is:', decode(text, shift_number))
        
        response = input('\nWould you like to go again? Type \'yes\' or \'no\': ' ).lower()
        
        if response == 'no':
            break