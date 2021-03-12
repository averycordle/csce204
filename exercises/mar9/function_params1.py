#Author: Avery Cordle

#make factorial more dynamic
def factorial(num):
    answer = 1

    if num<0:
        print("Invalid Num")
        return
    
    for i in range(1, num+1):
        answer *= i
    
    print(f"{num}! = {answer}")


# this is called passing in a parameter
factorial(7)