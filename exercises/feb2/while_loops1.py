#Author: Avery Cordle

userInput = input("Do you want to say hello: ").lower().strip()

while userInput == "yes":
    print("Hello")
    #now we must provide a way for the loop to stop
    userInput = input("Do you want to say hello again: ").lower().strip()

print("Goodbye")