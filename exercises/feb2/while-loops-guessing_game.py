#Author: Avery Cordle

import random

goal = random.randint(1,100)

#we don't want them to know the secret number
print(f"Number to guess is {goal}")

guess = int(input("Enter a number between 1 and 100: "))

#while they don't guess correctly
while guess != goal:
    #get feedback and a new guess
    print("Wrong")
    if guess<goal:
        print("Too low")
    elif guess>goal:
        print("Too high") 
    guess = int(input("Guess again: "))
print("Congrats! You got it right!")