import os
import subprocess
import random
from random import shuffle
import time

SCORE = 0

def conundrum_game():
    '''
    Generate scrambled, random word from the list of words. Count the number
    of tries by the user if incorrect, after 3 goes print the correct answer.
    '''
    word_list = ['apple', 'television', 'science', 'computer', 'kitchen',
    'xylophone', 'variable', 'question', 'tomorrow', 'standard', 'manipulate',
    'simple', 'expression', 'game']
    random_word = random.choice(word_list)
    scrambled_word = ''.join(random.sample(random_word, len(random_word)))
    guess = ''
    print(f'Your conundrum is: {scrambled_word}')
    tries = 3
    while tries >0:
        tries = tries -1
        guess = input('\nEnter your answer:')
        if guess == random_word:
            global SCORE
            print('\n **Congratulations!** You got it!')
            SCORE = SCORE + 1
            break
        else:
            print("\n Sorry, that's incorrect")

    print(f'\n The correct answer is: {random_word}')
     

def restart_game():
    '''
    Function to restart the game or exit
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
    
    



def main():
    '''
    Welcome message, rules and name input
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
        print ('Please only use letters for your name')
    print(f'Welcome {name}!')
    #print('MAIN SCORE: ', SCORE)
    time.sleep(1)
    display_rules()
    time.sleep(7)
    clear_screen()
    conundrum_game() 
    restart_game()
   
main()
