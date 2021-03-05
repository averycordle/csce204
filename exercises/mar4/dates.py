#Author: Avery Cordle

from datetime import date, time, datetime

todaysDate = date.today()
print(todaysDate)
print(todaysDate.strftime("%m/%d/%y"))
print(todaysDate.strftime("%A %B %d, %Y"))
print(todaysDate.strftime("%B %d: %A, Year: %y"))


todaysDateTime = datetime.now()
print(todaysDateTime.strftime("%B %d, %Y, %I:%M %p"))

halloween = date(2021,10,31)
meeting = time(14, 30) #2:30
appointment = datetime(2021, 3, 4, 14, 30)

birthdayInput = input("Enter Birthday (MM/DD/YYYY): ").strip()
birthday = datetime.strptime(birthdayInput, "%m/%d/%Y")#use the datetime to strip down the time to get what we need

print("Your birthday: " + birthday.strftime("%A %B %d, %Y"))

days = (appointment - datetime.now()).days
print(f"You have {days} till your appointment")

