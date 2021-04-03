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
    scores = []
    with open("assignments/assignment12/score.txt") as file:
        for line in file:
            scores.append(int(line))
    return scores

def save_score(scores):
    with open("assignments/assignment12/score.txt","w") as file:
        file.write(f"{scores[0]}\n")
        file.write(f"{scores[1]}\n")
        file.write(f"{scores[2]}\n")


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
scores = getScore()

while True:
    command = input("(P)lay or (Q)uit: ").strip().lower()

    if command == "q":
        break
    elif command != "p":
        print("Invalid Command")
        continue

    if playRound():
        print("Yay, you got it!")
        scores[1]+=1
    else:
        print("Sorry, incorrect")
        scores[2]+=1
    scores[0]+=1

save_score(scores)

print("Games Played: " + str(scores[0]), end="")
print("")
print("Games Won: " + str(scores[1]), end="")
print("")
print("Games Lost: " + str(scores[2]), end="")
print("")

print("Goodbye!")