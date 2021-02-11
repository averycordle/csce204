#Author: Avery Cordle

numGrades = int(input("How many grades would you like to enter: "))
sum = 0

for i in range(numGrades):
    grade = float(input(f"Enter grade {i+1}: "))
    while grade<0 or grade>100:
        print("Invalid grade")
        grade = float(input(f"Enter grade {i+1}: "))

    sum += grade

average = sum/numGrades
print(f"Average is: {average}")