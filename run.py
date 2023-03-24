# Python Libraries
import os
import random
import time
from rich.console import Console


# Global variable for scoring as per CI Student Support instruction
SCORE = 0
console = Console()

def scramble_word(word):
    '''
    Return a random word from the word list using the random sample method 
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
        guess = input('\nEnter your answer: ').strip().lower()
        if guess == random_word:
            global SCORE
            console.print('\n **Congratulations!** You got it!',
            style = "green")
            SCORE = SCORE + 1
            break
        else:
            console.print("\n Sorry, that's incorrect...", style="red")

    console.print(f'\n The correct answer is: [bold blue]{random_word}[/]')


def restart_game():
    '''
    Function to restart the game or exit on users choice.
    Check if input is valid, no whitespace and lowercase y or n.
    Print score if user chooses no or restart game if yes.
    '''
    while True:
        print('\nWould you like to play again?')
        console.print("\nEnter [green]'y'[/] for YES or [red]'n'[/] for NO:\n")
        user_choice = input().strip().lower()
        if user_choice == 'y':
            clear_screen()
            conundrum_game()
        elif user_choice == 'n':
            print(f'You got {SCORE} correct!')
            console.print('\nThank you for playing ! \n',style="reverse")
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
    checks if name is letters only, welcomes the user, rich syle added.
    '''
    console.print('---------------------------------',
    style="bold red on white ")
    console.print('         WELCOME TO THE          ',
    style="bold red on white")
    console.print('         CONUNDRUM GAME          ',
    style="bold red on white")
    console.print('---------------------------------',
    style="bold red on white")
    print('\nPlease enter your name:\n')
    name = ''
    while True:
        name = input()
        if name.isalpha():
            break
        print('\nPlease only use letters for your name')
    console.print(f'Welcome {name}!', style="bold red on white")
    time.sleep(1)
    display_rules()
    time.sleep(7)
    clear_screen()
    conundrum_game()
    restart_game()


main()
