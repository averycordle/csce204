#Author: Avery Cordle
def getDictionary():
    dictionary = {}
    try:
        with open("assignments/assignment11/words.txt") as file:
            for line in file:
                data = line.split(':')
                states = data[0].strip()
                capitals = data[1].strip()
                dictionary[states] = capitals
            return dictionary
    except FileNotFoundError:
        print("Sorry, that is not in the dictionary. Check permissions.")
        return dictionary

def getDefinition(dictionary):
    state = input("Enter state name to define it's capital: ").strip().lower()
    if state in dictionary:
        print(f"{dictionary[state]}") 
    else:
        print(f"Sorry, {state} is not in our state list.")

def displayDictionary(dictionary):
    print("Display states and their capital cities!")
    for state in dictionary:
        capitals = dictionary[state]
        print(f"{state}: {capitals}")

print("Our State Capital Dictionary")
dictionary = getDictionary()

while True:
    userInput = input("Would you like to (V)iew, (D)efine, or (Q)uit: ").lower().strip()
    if userInput == "q":
        print("Good Bye!")
        break
    elif userInput == "v":
        displayDictionary(dictionary)
    elif userInput == "d":
        getDefinition(dictionary)