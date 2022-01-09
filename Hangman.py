import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words) # randomly choses something from the list
    while '-' in word or '' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # What the user has guessed

    lives  = 6

    # Get user input
    while len(word_letters) > 0:
        # Used letters
        print("You have used these leters: ", ' '.join(used_letters))
        # What the current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet == used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print("You have already used that letter. Please try again.")
        else:
            print("Invalid character. Please try again.")
    # gets here when len(word_letters) == 0

hangman()

user_input = input("Type something: ")
print(user_input)