
# NAME OF AUTHOR:  Cameron Reid
# NAME OF THE PROGRAM:  Q3Addition
# DATE OF CREATION:  December 6
# PURPOSE OF PROGRAM:  TO add 2 random numbers

# VARIABLE DEFINITION
# num1 and num2
# INPUT
import random
from _ast import If
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
# PROCESSING
print("What's the sum of the two numbers?")
print(str(num1) + ' + ' + str(num2) + ' = ' )
result = int(input())
# OUTPUT
if result == (num1 + num2) :
    print("Correct!!")
else: 
    print("Incorrect, try again")