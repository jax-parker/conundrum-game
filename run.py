#Import necessary libraries
#Welcome message
#User inputs name (input valid?)
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

#Create a list of words to randomly be chosen
WORDS = ('apple', 'telvision', 'science', 'computer', 'kitchen', 'xylophone')

def main():
    '''
    Welcome message, rules and name input
    '''
    print('---------------------------------\n')
    print('         WELCOME TO THE          ')
    print('         CONUNDRUM GAME          \n')
    print('----------------------------------\n')
    print('Please enter your name:')
    name = ''
    while True:
        name = input()
        if name.isalpha():
            break
        print ('Please only use letters for your name\n')
    print(f'Welcome {name}!')

    time.sleep(1.2)

    main()

    
