#Author: Avery Cordle

import random

print("Welcome to our multiplication game")

command = input("Shall we ask you a question (Y)es or (N)o: ").lower().strip()

while command == "y":
    num1 = random.randint(1,12)
    num2 = random.randint(1,12)
    guess = input(str(num1) + " * " + str(num2) + " = ")
    answer = str(num1*num2)
    if guess == answer:
        print("You got it!")
        command = input("Shall we ask you a question (Y)es or (N)o: ").lower().strip()
    else:
        print(f"Sorry, the correct answer was {answer}")
        command = input("Shall we ask you a question (Y)es or (N)o: ").lower().strip()

print("Goodbye")