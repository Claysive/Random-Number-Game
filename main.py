#author: Claysive
#description: just a simple random number guessing game
#TODO: update to include a user number and have the computer guess it. should include an option of which game to play - first half done

import random #imports the random module to generate a random number using 'randint'
import pyinputplus as pyip

#function to generate a random number btwn one and a hundred. may update it to allow the number range to be user defined
def get_guess():
    guess = random.randint(1, 100)
    return guess

#this function allows the user to guess a number that the computer randomly generates. provides feedback to the user to determine if their number was too high or too low. 
def player_guess():
    comp_guess = get_guess() #shoud prob change this variable name
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
            print(f"Congrats! Looks like you were smarter than me after all! My number was {comp_guess}\n")
            break
        if guessCounter > 5:
            print(f"Better luck next time peasant! My number was {comp_guess}!\n")

#this function allows the user to think of a number and have the computer guess it. the user must provide feedback to tell the computer if it's guess was too high or too low or correct. still need to add some exception handling, but currently functions as intended
def player_number():
    high = 50
    low = 1
    feedback = ''
    comp_guess_count = 1

    print(f"This time, let's try something different. You'll think of a number between {low} and {high} and I'll guess it\nwithin 8 tries, or you win. You'll just have to provide some feedback to help me along.\n(H) will be for a guess that's too high, (L) will be for a guess that's too low, and (C) will be for a correct guess!\n")

    #TODO: add an on_ready function to start the loop, currently, once the funtion is called, the welcome message shows and instanly continues on with a guess. gives the user no time to actually think of a number. silly, but could be usefull. add a message to be displayed once the computer loses, may also increase the number of guesses for the computer

    comp_num = random.randint(low,high)

    while comp_guess_count <= 8:
      print(f"My guess number {comp_guess_count} is: {comp_num}! How did I do? Was it too(H)igh, too (L)ow or (C)orrect?")
      feedback = input(f"Your response: ").lower()
      
      if feedback == 'h':
        high = comp_num -1
      elif feedback == 'l':
        low = comp_num + 1
      else:
        print(f"I knew I was smarter than you!")
        break
      
      comp_num = random.randint(low,high)
      comp_guess_count = comp_guess_count + 1

#set the welcome message of the game, named title, can possibly change the name since you know, its not really the title of the game :) 
title = f"Welcome to the number guessing game! You'll have 5 trys to guess my number.\n" \
f"Are you smarter than me? Let's find out! The number is between 1 and 100. Good Luck!\n"

#print the welcome message of the game
print(title)

#run the main functions of the game
player_guess()
player_number()