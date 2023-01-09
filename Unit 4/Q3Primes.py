# Read the two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Iterate over the range of numbers between the two numbers (inclusive)
for num in range(num1, num2+1):
  # Check if the current number is prime
  is_prime = True
  for divisor in range(2, int(num ** 0.5) + 1):
    if num % divisor == 0:
      is_prime = False
      break
  # If the number is prime, print it
  if is_prime:
    print(num)