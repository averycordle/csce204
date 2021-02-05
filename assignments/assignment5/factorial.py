#Author: Avery Cordle

print("Welcome to our factorial generator")
userNumber = int(input("Enter Number: "))
sumFactorial = 1

for i in range(1, userNumber + 1):
    sumFactorial = sumFactorial*i

print(f"Factorial of {userNumber} is {sumFactorial}")