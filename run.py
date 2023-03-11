#Import necessary libraries - done
#Welcome message - done
#User inputs name (input valid?) - done
#Define the main function (def conundrum game)
#Define the variables (word list)
#Pick random word
#Scramble word
#Print scrambled word
#User input guess (input valid?)
#Check if guess is correct
#Print message to user
#Ask if user would like to play again (input valid?)

'''Python Libraries'''
import os
import random
from random import shuffle
import time

def conundrum_game():
    '''
    Generate scrambled, random word from the list of words.
    '''
    word_list = ['apple', 'telvision', 'science', 'computer', 'kitchen', 'xylophone']
    random_word = random.choice(word_list)
    scrambled_word = ''.join(random.sample(random_word, len(random_word)))
    guess = ''
    print(scrambled_word)
 
   





def display_rules():
    '''
    Displays the rules of the game
    '''
    print('HOW TO PLAY:')
    print('We have scrambled up the letters of a word')
    print('Unscramble the letters and enter your guess below')
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
    time.sleep(1)
    display_rules()
    conundrum_game() 
   
main()

    
