from question import Question
import random
FILE_NAME = "apr13/questions.txt"

def get_questions():
    questions = []
    with open(FILE_NAME)as file:
        for line in file:
            data = line.split(',')
            prompt = data[0].strip()
            answer1 = data[1].strip()
            answer2 = data[2].strip()
            answer3 = data[3].strip()
            answer4 = data[4].strip()
            correct_ans = int(data[5].strip())
            question = Question(prompt, answer1, answer2, answer3, answer4, correct_ans)
            questions.append(question)
    return questions

questions = get_questions()

print("Trivia Game!")

while True:
    command = input("(P)lay or (Q)uit: ").lower().strip()
    if command == "q":
        break
    elif command != "p":
        print("Invalid Input")
        continue
    
    question = random.choice(questions)
    print(question.prompt)
    question.display_answers()
    user_ans = int(input("Enter numerical answer: "))

    if question.correct_answer == user_ans - 1:
        print("Nice")
    else:
        print("Wrong")

print("Goodbye")