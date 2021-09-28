import random

def get_guess():
    guess = random.randint(1, 100)
    return guess

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

title = f"Welcome to the number guessing game! You'll have 5 trys to guess my number.\n" \
f"Are you smarter than me? Let's find out! The number is between 1 and 100. Good Luck!"

print(title)

player_guess()