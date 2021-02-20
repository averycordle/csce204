#Author: Avery Cordle

listTodo = []
listCompleted = []

print("Welcome to your todo list")

while True:
    #q option (aka break)
    firstInput = input("(V)iew, (A)dd, (R)emove, or (Q)uit: ").lower().strip()
    if firstInput == "q":
        break
    #view option
    elif firstInput == "v":
        secondInput = input("View (T)odos or (C)ompleted Items? ").lower().strip()
        #view todos
        if secondInput == "t":
            if len(listTodo) == 0:
                print("You have no todos")
            else:
                for i in range(len(listTodo)):
                    print(f"{i+1}. {listTodo[i]}")
        #view completed
        elif secondInput == "c": 
            if len(listCompleted) == 0:
                print("You have no done items")
            else:
                for j in range(len(listCompleted)):
                    print(f"-{listCompleted[j]}")
        #invalid return
        else:
            print("Invalid input, try v or c next time")
    #add option
    elif firstInput == "a":
        thirdInput = input("Enter todo: ").lower().strip()
        if (thirdInput != "" and (thirdInput in listTodo) == False):
            listTodo.append(thirdInput)
        else:
            print(f"Invalid input, either empty or {thirdInput} was already in the list")
    #remove option
    elif firstInput == "r":
        fourthInput = input("Enter todo: ").lower().strip()
        if (fourthInput != "" and (fourthInput in listTodo) == True):
            listTodo.remove(fourthInput)
            listCompleted.append(fourthInput)
        else:
            print(f"Sorry, {fourthInput} was either not in the todo list or already completed")
    else:
        print("Invalid Command, try entering v, a, r, or l")
print("Goodbye")