#Python Libraries
import os
import subprocess
import random
from random import shuffle
import time

# Global variable for scoring as per Student support advice
SCORE = 0


def scramble_word(word):
    '''
    Return a scrambled word from the random word
    '''
    return ''.join(random.sample(word, len(word)))


def conundrum_game():
    '''
    Generate random word from the dict list of words and scramble it.
    User correct - display message and answer.
    Count the number of tries by the user if incorrect.
    After 3 goes print the correct answer.
    '''
    word_list = [
        'apple', 'simple', 'computer', 'tomorrow', 'sunset',
        'variable', 'television', 'history', 'switch'
        ]
    word_dict = {
        word: scramble_word(word) for word in word_list
        }
    random_word = random.choice(list(word_dict.keys()))
    scrambled_word = word_dict[random_word]

    guess = ''
    print(f'Your conundrum is: {scrambled_word}')
    tries = 3
    while tries > 0:
        tries = tries - 1
        guess = input('\nEnter your answer:')
        if guess == random_word:
            global SCORE
            print('\n **Congratulations!** You got it!')
            SCORE = SCORE + 1
            break
        else:
            print("\n Sorry, that's incorrect, try again...")

    print(f'\n The correct answer is: {random_word}')


def restart_game():
    '''
    Function to restart the game or exit on users choice.
    Check if input is valid, no whitespace and lowercase y or n.
    Print score if user chooses no or restart game if yes.
    '''
    while True:
        print('\nWould you like to play again?')
        print("\nEnter 'y' for YES or 'n' for NO:\n")
        user_choice = input().strip().lower()
        if user_choice == 'y':
            clear_screen()
            conundrum_game()
        elif user_choice == 'n':
            print(f'You got {SCORE} correct!')
            print('\nThank you for playing\n')
            break
        else:
            print("Invalid answer. Press 'y' to restart or 'n' to exit game.")


def clear_screen():
    '''
    Clears the screen at the start of the game and after each correct answer
    '''
    if os.name == 'nt':
        os.system('clear')
    else:
        os.system('clear')


def display_rules():
    '''
    Displays the rules of the game
    '''
    print('\nHOW TO PLAY:')
    print('We have scrambled up the letters of a word.\n')
    print('Unscramble the letters and enter your guess below\n')
    print('You have 3 tries to guess the word - Good Luck!\n')
    print('Get ready...\n')


def main():
    '''
    Displays the welcome message, asks user to input name,
    checks if name is letters only, welcomes the user.
    '''
    print('---------------------------------')
    print('         WELCOME TO THE          ')
    print('         CONUNDRUM GAME          ')
    print('----------------------------------')
    print('Please enter your name:')
    name = ''
    while True:
        name = input()
        if name.isalpha():
            break
        print('Please only use letters for your name')
    print(f'Welcome {name}!')
    time.sleep(1)
    display_rules()
    time.sleep(7)
    clear_screen()
    conundrum_game()
    restart_game()


main()
