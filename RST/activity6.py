# NAME OF AUTHOR: Cameron Reid
# NAME OF THE PROGRAM: Activity6
# DATE OF CREATION:  January 16th, 2023
# PURPOSE OF PROGRAM: engaging number guessing game

# VARIABLE DEFINITION
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

import random

#Input
def guessing_game():
    number = random.randint(num1, num2)
    guess = None
    attempts = 0
    # Processing
    while guess != number:
        guess = int(input("Guess a number between num1 and num2: "))
        attempts += 1
        if guess < number:
            print("Too low, try again!")
        elif guess > number:
            print("Too high, try again!")
    # Output      
    print("You guessed the correct number in", attempts, "attempt(s)!")

guessing_game()
