var1 = 0
var2 = 0
var3 = 0
var4 = 0
var5 = 0
sum = 0
print("enter first number")
var1 = int(input())

print("enter Second number")
var2 = int(input())

print("enter Third number")
var3 = int(input())

print("enter Fourth number")
var4 = int(input())

print("enter Fifth number")
var5 = int(input())

n = int(input("Enter number"))

print("The Average is:")
sum = 0
# loop from 1 to n
for num in range(1, n + 1, 1):
    sum = sum + num
print("Sum of first ", n, "numbers is: ", sum)
average = sum / n
print("Average of ", n, "numbers is: ", average)

sum = var1 + var2 + var3 + var4 + var5 
print("The sum is: ")
print(sum)

