#Author: Avery Cordle

#grade calculator
print("grade calculator")
assignments = float(input("Enter your assignments grade: "))
exercises = float(input("Enter your exercises grade: "))
quizzes = float(input("Enter your quizzes grade: "))
midterm = float(input("Enter your midterm grade: "))
final = float(input("Enter your final exam grade: "))

finalGrade = round(assignments *.25 + exercises *.1 + quizzes *.15 + midterm *.25 + final *.25, 1)
print(f"Your final grade for CSCE 204 is {finalGrade}")







