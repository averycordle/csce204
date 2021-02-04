#Author: Avery Cordle
#for loop is for NUMBERS and COUNTING

"""count from 1 to 10
for i in range(1,11):
    print(i)
"""

"""
#the last two is called the step and this is what you count by
for i in range(2,21,2):
    print(i)
"""

"""
for i in range (10,0,-1):
    print(i)
"""

"""
#sum the numbers 1 through 10
sum = 0
for i in range(1,11):
    sum+=i

print(f"Sum of numbers 1 through 10: {sum}")
"""

"""
#sum the number the user gives us
sum = 0
userNum = int(input("Enter number: "))
for i in range(1,userNum + 1):
    sum+=i

print(f"Sum of numbers 1 through {userNum}: {sum}")
"""

#sum the numbers user start to user end
sum = 0
userStart = int(input("Enter number: "))
userEnd = int(input("Enter number: "))
for i in range(userStart, userEnd+1):
    sum+=i

print(f"Sum of numbers {userStart} through {userEnd}: {sum}")
