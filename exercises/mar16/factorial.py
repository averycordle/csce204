#Author: Avery Cordle

def factorial(num):
    answer = 1

    for i in range(1, num+1):
        answer *= i 

    #without having to write a print() statement
    #can only have one "return ..." for a function but can have multiple returns
    return answer

result = factorial(7)

print(f"7! = {result}")
