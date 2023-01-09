import random

while True:
  # Generate a random question
  question_type = random.randint(1, 2)
  if question_type == 1:
    # Generate an addition question
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"What is {num1} + {num2}?"
    answer = num1 + num2
  else:
    # Generate a multiplication question
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    question = f"What is {num1} x {num2}?"
    answer = num1 * num2
 
  # Print the question and read the user's response
  print(question)
  response = int(input())
 
  # Check the user's answer and provide feedback
  if response == answer:
    print("Correct!")
  else:
    print("Incorrect")
 
  # Check if the user wants to exit the game
  exit_response = input("Enter 'exit' to exit the game, or press enter to continue: ")
  if exit_response.lower() == "exit":
    break