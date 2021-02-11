#Author: Avery Cordle
"""
while True:
    grade = float(input("Enter grade between 0 and 100: "))
    
    if grade >=0 and grade <=100:
        break
    #break means to get out of the loop
    else:
        print("Invalid grade, please enter a number in the range: 0-100")
        #you really don't even need the "else"
"""

grade = float(input("Enter grade between 0 and 100: "))

while grade<0 or grade>100:
    print("Invalid grade, please enter a number in the range: 0-100")
    grade = float(input("Enter grade between 0 and 100: "))

