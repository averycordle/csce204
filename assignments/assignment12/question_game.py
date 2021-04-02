#Author:Avery Cordle

import random

def getQuestions():
    questions = {}
    with open("assignments/assignment12/trivia.txt") as file:
        for line in file:
            data = line.split(':')
            question = data[0].strip()
            answer = data[1].strip()
            questions[question] = convertToBool(answer)
        return questions

def getScore():
    with open("assignments/assignment12/score.txt") as file:
        for line in file:
            return int(line)

def save_score(score):
    with open("assignments/assignment12/score.txt","w") as file:
        file.write(f"{score}\n")
        file.write(f"{wins}\n")
        file.write(f"{losses}\n")

def convertToBool(answer):
    if answer == "true":
        return True
    else:
        return False
    
def playRound():
    question = random.choice(list(questions.keys()))
    userAns = input(f"True or False: {question} ").strip().lower()
    compAns = questions.get(question)

    if convertToBool(userAns) == compAns:
        return True
    else:
        return False

print("Welcome to our Trivia Game!")

questions = getQuestions()
score = getScore()
wins = getScore()
losses = getScore()

while True:
    command = input("(P)lay or (Q)uit: ").strip().lower()

    if command == "q":
        break
    elif command != "p":
        print("Invalid Command")
        continue

    if playRound():
        print("Yay, you got it!")
        wins+=1
    else:
        print("Sorry, incorrect")
        losses+=1
    score+=1

save_score(score)

with open("assignments/assignment12/score.txt") as file:
    for line in file:
        print("Games Played: " + line, end="")
        print("Games Won: " + line, end="")
        print("Games Lost: " + line, end="")

print("Goodbye!")