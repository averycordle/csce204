#Author: Avery Cordle

#get grades from a user (how many them want)
#sum them and calculate the average

print("Grades Program")
gradeNumber = int(input("How many grades: "))
gradeTotal= 0


for i in range(1,gradeNumber + 1):
    gradeTotal += int(input(f"Enter grade {i}: "))
average = gradeTotal/gradeNumber
print(f"Your average is {round(average,1)}")