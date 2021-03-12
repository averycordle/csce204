#Author: Avery Cordle

def decimal_to_binary():
    num = int(input("Enter decimal number: "))
    answerChain = ""
    one = "1"
    zero = "0"
    while num>=1:
        remainder = num%2
        num//=2
        for i in range(1):
            if remainder %2 ==0:
                answerChain = zero + answerChain
            elif remainder %2 !=0 or remainder==1: 
                answerChain = one + answerChain
    print(f"{answerChain}")

def binary_to_decimal():
    num = int(input("Enter binary number: "))
    expo=2
    result = 0
    counter = 0
    while num>=1:
        remainder = num%2
        num//=10
        for i in range(1):
            remainder*=(expo**counter)
            result+=remainder
            counter+=1
    print(result)

print("Calculator")
while True:
    userInput = input("Convert from Binary to Decimal (BtD) or from Decimal to Binary (DtB), or (Q)uit: ").lower().strip()
    if userInput == "btd":
        binary_to_decimal()
    elif userInput == "dtb":
        decimal_to_binary()
    elif userInput =="q":
        break
    else:
        print("Invalid Command")
print("Goodbye")