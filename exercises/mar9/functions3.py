#Author: Avery Cordle

def factorial():
    num = int(input("Enter number: "))
    #we always start it at 1
    answer = 1

    if num < 1:
        print("Invalid number")
        #return takes you out of the function
        return
    
    for i in range(1, num+1):
        answer*=i

    print(f"{num}! = {answer}")

def power():
    base = int(input("Enter base number: "))
    expo = int(input("Enter exponent: "))
    answer =1

    if base < 1 or expo < 1:
        print("Invalid number")
        return

    for i in range(expo):
        answer*=base

    print(f"{base}^{expo} = {answer}")

def sumS():
    numSum = int(input("Enter number: "))
    answer = 0

    if numSum < 1:
        print("Invalid number")
        return

    for i in range(1, numSum+1):
        answer+=i
    
    print(f"Sum of 1...{numSum} is {answer}")

print("Welcome to Math!")
while True:
    userInput = input("Compute (F)actorial, (P)ower, (S)um, or (Q)uit: ")
    if userInput == "f":
        factorial()
    elif userInput == "p":
        power()
    elif userInput == "s":
        sumS()
    elif userInput == "q":
        break
    else:
        print("Invalid Input")
print("Goodbye")