import pandas as pd

nato = pd.read_csv('data/nato_phonetic_alphabet.csv')

# Create mapping of letter to NATO word
mapping = {}
for (index, row) in nato.iterrows():
    mapping[row.letter.lower()] = row.code


word = input('Enter a word to be converted into the NATO alphabet: ').lower()

# Create list where each index is NATO word of letter in the user's word
result = [mapping[letter] for letter in word]

print(result)