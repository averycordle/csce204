#Author: Avery Cordle

toys = ["ball", "car", "doll", "bubbles", "crayons"]

print("Welcome to our toy store")

while True:
    command = input("(L)ist, (A)dd, (R)emove, or (Q)uit: ").lower().strip()
    if command == "q":
        break
    elif command == "l":
        for i in range (len(toys)):
            print(f"{i+1}, {toys[i]}")
    elif command == "a":
        userInput = input("What toy would you like to add? ").lower().strip()
        if (userInput != "" and (userInput in toys) == False):
            toys.append(userInput)
        else:
            print("Invalid toy name, either empty or already in the list")
    elif command == "r":
        userInputR = input("What toy would you like to remove? ").lower().strip()
        if userInputR in toys:
            toys.remove(userInputR)
        else:
            print("Invalid toy name, either empty or noting the list")
    else: 
        print("Invaid input, try again")
    
print("Goodbye")