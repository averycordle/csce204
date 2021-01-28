#Author: Avery Cordle

print("My Dating App!")
relStatus = input("Are you married? ").lower().strip()

if relStatus != "yes":
    print("Welcome")
else:
    print("Go away")