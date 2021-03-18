#Author: Avery Cordle
import random
def get_players_choice():
    playerChoice = input("Enter (R)ock, (P)aper, or (S)cissors: ").lower().strip()
    if playerChoice == True:
        return False
    return playerChoice

def get_comp_choice():
    choiceS = ["r","p","s"]
    computerChoice = random.choice(choiceS)
    print(f"Computer choose: {computerChoice}")
    return computerChoice

def play_game(play1, play2):
    if playerPick == computerPick:
        return 0
    elif playerPick == "r" and computerPick == "s" or playerPick == "p" and computerPick == "r" or playerPick == "s" and computerPick == "p":
        return 1
    elif playerPick == "r" and computerPick == "p" or playerPick == "p" and computerPick == "s" or playerPick == "s" and computerPick == "r":
        return 2

print("Welcome to Rock Paper Scissors")
userInput = input("(P)lay or (Q)uit: ").lower().strip()
userWon = 0
compWon = 0
tiedUp = 0
while True:
    if userInput == "p":
        playerPick = get_players_choice()
        computerPick = get_comp_choice()
        result = play_game(playerPick, computerPick)
        if result == 0:
            print("Tie!")
            tiedUp+=1
        elif result == 1:
            print("You Won!")
            userWon+=1
        elif result == 2:
            print("Computer Won!")
            compWon +=1
        userInput = input("(P)lay or (Q)uit: ").lower().strip()
    elif userInput == "q":
        break
    else:
        print("Invalid command")
        userInput = input("(P)lay or (Q)uit: ").lower().strip()

print(f"""
You won {userWon} rounds
The computer won {compWon} rounds
You tied {tiedUp} rounds
""")