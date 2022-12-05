import random
from _ast import If
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
print("What's the sum of the two numbers?")
print(str(num1) + ' + ' + str(num2) + ' = ' )
result = int(input())

if result == (num1 + num2) :
    print("Correct!!")
else: 
    print("Incorrect, try again")