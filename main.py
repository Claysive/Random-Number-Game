#author: Claysive
#description: just a simple random number guessing game
#TODO: update to include a user number and have the computer guess it. should include an option of which game to play

import random #imports the random module to generate a random number using 'randint'

#function to generate a random number btwn one and a hundred. may update it to allow the number range to be user defined
def get_guess():
    guess = random.randint(1, 100)
    return guess

#this is the main function. will hopefully update soon with the todo from above
def player_guess():
    comp_guess = get_guess()
    playerGuess = 0
    guessCounter = 1

    while guessCounter <= 5:
        playerGuess = int(input(f"Enter guess number {guessCounter}: "))
        guessCounter = guessCounter + 1
        if playerGuess < comp_guess and guessCounter != 6:
            print(f"You're guess was too low, try again!")
        elif playerGuess > comp_guess and guessCounter != 6:
            print(f"Your guess was too high, try again!")
        elif playerGuess == comp_guess:
            print(f"Congrats! Looks like you were smarter than me after all! My number was {comp_guess}")
            break
        if guessCounter > 5:
            print(f"Better luck next time peasant! My number was {comp_guess}!")

#set the title of the game
title = f"Welcome to the number guessing game! You'll have 5 trys to guess my number.\n" \
f"Are you smarter than me? Let's find out! The number is between 1 and 100. Good Luck!"

#print the title of the game
print(title)

#run the main function of the game
player_guess()