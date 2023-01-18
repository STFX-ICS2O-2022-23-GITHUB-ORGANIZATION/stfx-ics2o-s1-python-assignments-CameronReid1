# NAME OF AUTHOR: Cameron Reid
# NAME OF THE PROGRAM:hangman.py
# DATE OF CREATION:  January 17th, 2023
# PURPOSE OF PROGRAM: To create a guessing game



# VARIABLE DEFINITIOM
import random

# INPUT

def hangman():
    word_list = ["python", "javascript", "computer", "programming", "coding", "machinelearning", "artificialintelligence", "deeplearning", "neuralnetwork", "algorithm"]
    word = random.choice(word_list)
    word_letters = set(word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set()
    tries = 6
    # PROCESSING

    print("The word contains", len(word), "letters.")
    while len(word_letters) > 0 and tries > 0:
        print("You have", tries, "tries left.")
        if len(used_letters) > 0:
            print("Used letters:", " ".join(used_letters))
        guess = input("Please enter a letter: ").lower()
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
                print("Correct!")
            else:
                print("Incorrect!")
                tries -= 1
        else:
            print("You already used that letter.")
    if tries > 0:
        # OUTPUT

        print("Congratulations! The word was", word)
    else:
        print("Sorry, the word was", word)

hangman()







# OUTPUT

