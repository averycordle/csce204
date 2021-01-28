#Author: Avery Corde

print("Calculate your grade!")
assignments = float(input("Enter your assignment grade: "))
quizzes = float(input("Enter your quizzes grade: "))
midterm = float(input("Enter your midterm grade: "))
final = float(input("Enter your final grade: "))

finalGrade = assignments*.4 + quizzes*.1 + midterm*.25 + final*.25
letterGrade = "F"

print(f"Your final grade is {round(finalGrade, 1)}")

if finalGrade >=89.5:
    letterGrade = "A"
elif finalGrade >=79.5:
    letterGrade = "B"
elif finalGrade >=69.5:
    letterGrade = "C"
elif finalGrade >=59.5:
    letterGrade = "D"
else:
    letterGrade = "F"

print(f"Letter Grade is {letterGrade}")