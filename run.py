#Import necessary libraries - done
#Welcome message - done
#User inputs name (input valid?) - done
#Define the main function (def conundrum game) - done
#Define the variables (word list) - done
#Pick random word - done
#Scramble word - done
#Print scrambled word - done
#User input guess (input valid?)
#Check if guess is correct - done
#Print message to user - done
#Ask if user would like to play again (input valid?) - done

'''Python Libraries'''
import os
import random
from random import shuffle
import time

SCORE = 0

def conundrum_game():
    '''
    Generate scrambled, random word from the list of words.
    '''
    word_list = ['apple', 'television', 'science', 'computer', 'kitchen',
    'xylophone', 'variable', 'question', 'tomorrow', 'standard', 'manipulate',
    'simple', 'expression', 'game']
    random_word = random.choice(word_list)
    scrambled_word = ''.join(random.sample(random_word, len(random_word)))
    guess = ''
    # SCORE = 0
    print(f'Your conundrum is: {scrambled_word}')
    tries = 3
    while tries >0:
        tries = tries -1
        guess = input('Enter your answer:')
        if guess == random_word:
            global SCORE
            print('\n **Congratulations!** You got it!')
            SCORE = SCORE + 1
            print('INCREMENTED SCORE: ', SCORE)
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
            print('SCORE when Y is clicked: ', SCORE)
            conundrum_game()
        elif user_choice == 'n':
            print('THE SCORE IS: ', SCORE)
            print(f'You got {SCORE} correct!')
            print('Thank you for playing\n')
            break
        else:
            print("Invalid answer. Press 'y' to restart or 'n' to exit game.")

def display_rules():
    '''
    Displays the rules of the game
    '''
    print('HOW TO PLAY:')
    print('We have scrambled up the letters of a word.\n')
    print('Unscramble the letters and enter your guess below\n')
    print('You have 3 tries to guess the word - Good Luck!')



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
    print('MAIN SCORE: ', SCORE)
    time.sleep(1)
    display_rules()
    conundrum_game() 
    restart_game()
   
main()
