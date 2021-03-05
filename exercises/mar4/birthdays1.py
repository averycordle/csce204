#Author: Avery Cordle

from datetime import date

birthdays = [
    date(2021, 7, 23), date(2021, 2, 25), date(2021, 10, 9), date(2021, 4, 29), date(2021, 9, 20),  date(2021, 10, 20), date(2021, 11, 29)
]

closestBirthday = date(2021, 12, 31)

for birthday in birthdays:
    daysTilClosest = (closestBirthday - date.today()).days
    daysTillBirthday = (birthday - date.today()).days

    #birthday already passed
    if daysTillBirthday<0:
        continue #go to the next item in the list

    #what we want
    if daysTillBirthday<daysTilClosest:
        closestBirthday = birthday
print ("Closest birthday is: " + closestBirthday.strftime("%m/%d/%Y"))
