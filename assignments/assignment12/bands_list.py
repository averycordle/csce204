#Author: Avery Cordle  
FILE_NAME = "assignments/assignment12/bands.txt"

def writeBands(bands):
    with open(FILE_NAME, "w") as file:
        for band in bands:
            file.write(band + "\n")

def readBands():
    bands = []
    with open(FILE_NAME) as file:
        for line in file: 
            line = line.replace("\n","").strip()
            bands.append(line)
    return bands

def listBands(bands):
    for i in range(len(bands)):
        print(f"- {bands[i]}")

def addBands(bands):
    band = input("Enter band: ").strip()
    bands.append(band)
    writeBands(bands)
    print(f"{band} was added.")
    return bands

def deleteBands(bands):
    index = input("Enter band name: ")

    if index in bands:
        band = bands.remove(index)
        writeBands(bands)
        print(f"{index} was deleted.")
    else: 
        print(f"Sorry, {index} was not found on the list")
    return bands

while True:
    userInput = input("Enter (L)ist, (A)dd, (D)elete, or (Q)uit: ").lower().strip()
    bands = readBands()

    if userInput == "l":
        listBands(bands)
    elif userInput == "a":
        bands = addBands(bands)
    elif userInput == "d":
        bands = deleteBands(bands)
    elif userInput == "q":
        break
    else:
        print("Invalid command, try again.")

print("Goodbye")














