# Guessing game using random generated number

import random

numberToGuess = random.randint(1, 100)

while True:
    guess = input("Guess the number: ")
    if guess.isdigit():
        guess = int(guess)
        if guess == numberToGuess:
            print("Correct")
            # if true exit loop
            break
        elif guess < numberToGuess:
            print('Guess higher')
        else:
            print("Guess lower")
    else:
        print("Must be a number (1-100)")