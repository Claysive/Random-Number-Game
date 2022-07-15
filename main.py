#author: Claysive
#description: just a simple random number guessing game
#TODO: update to include a user number and have the computer guess it. should include an option of which game to play - first half done, added the user number and gave time to make a guess.

import random  #imports the random module to generate a random number using 'randint'
import pyinputplus as pyip  #imports the pyinputplus module, used for input validation


#function to generate a random number btwn one and a hundred. may update it to allow the number range to be user defined
def get_guess():
    high = 100
    low = 1
    guess = random.randint(low, high)
    return guess


#this function allows the user to guess a number that the computer randomly generates. provides feedback to the user to determine if their number was too high or too low.
def player_guess():
    comp_guess = get_guess()  #shoud prob change this variable name
    playerGuess = 0
    guessCounter = 1

    print(
        f'\nMy number is between 1 and 100. You have 8 guesses. Good luck to you!'
    )
    while guessCounter <= 8:
        playerGuess = pyip.inputInt(
            prompt=f"Enter guess number {guessCounter}: ")
        guessCounter = guessCounter + 1
        if playerGuess < comp_guess and guessCounter != 9:
            print(f"You're guess was too low, try again!")
        elif playerGuess > comp_guess and guessCounter != 9:
            print(f"Your guess was too high, try again!")
        elif playerGuess == comp_guess:
            print(
                f"Congrats! Looks like you were smarter than me after all! My number was {comp_guess}\n"
            )
            break
        if guessCounter > 8:
            print(
                f"Better luck next time peasant! My number was {comp_guess}!\n"
            )


#this function allows the user to think of a number and have the computer guess it. the user must provide feedback to tell the computer if it's guess was too high or too low or correct.
def player_number():
    high = 50
    low = 1
    feedback = ''
    comp_guess_count = 1

    print(
        f"\nYou'll think of a number between {low} and {high} and I'll guess it\nwithin 8 tries, or you win. You'll just have to provide some feedback to help me along.\n(H) will be for a guess that's too high, (L) will be for a guess that's too low, and (C) will be for a correct guess!\n"
    )

    #TODO: add a message to be displayed once the computer loses, may also increase the number of guesses for the computer
    comp_num = random.randint(low, high)

    input(f'Think of a number and press Enter when ready...')

    while comp_guess_count <= 8:
        print(
            f"My guess number {comp_guess_count} is: {comp_num}! How did I do? Was it too (H)igh, too (L)ow or (C)orrect?"
        )
        feedback = pyip.inputChoice(['h', 'l', 'c']).lower()

        if feedback == 'h':
            high = comp_num - 1
        elif feedback == 'l':
            low = comp_num + 1
        else:
            print(f"I knew I was smarter than you!")
            break

#checks to make sure that the range for the random function doesn't get out of whack and throw an error. prob needs a check for going to high as well, still needs a few more tests.
        if low > high:
            print(
                'Oopps, looks like you messed up somewhere, better luck next time!'
            )
            break

        comp_num = random.randint(low, high)
        comp_guess_count = comp_guess_count + 1


#set the welcome message of the game, named title, can possibly change the name since you know, its not really the title of the game :)
title = f"Welcome to the number guessing game! You can pick to either guess my number\nor have me guess yours. You'll have 8 guesses as will I. Good luck!"


def run_game():
    print(title)
    print(
        f'\nWould you like to have me pick a number and you guess it, or you pick a number\nand I guess it?'
    )
    game_ch = pyip.inputChoice(['You', 'Me']).lower()

    if game_ch == 'you':
        player_guess()
    else:
        player_number()


run_game()
#print the welcome message of the game
#print(title)

#run the main functions of the game
#player_guess()
#player_number()
