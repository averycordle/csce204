#Author: Avery Cordle

#difference is we're running a dictionary here

from datetime import date

birthdays = {
    "Sarah": date(2021, 2, 25), 
    "Toby": date(2021, 10, 9), 
    "David": date(2021, 9, 20),  
    "Abbi": date(2021, 10, 20), 
    "Rachel": date(2021, 11, 29),
    "Sam": date(2021, 7, 23)
}

closestBirthday = date(2021, 12, 31)
closestFriend = ""

for person in birthdays:
    birthday = birthdays[person]
    daysTilClosest = (closestBirthday - date.today()).days
    daysTillBirthday = (birthday - date.today()).days

    #birthday already passed
    if daysTillBirthday<0:
        continue #go to the next item in the list

    #what we want
    if daysTillBirthday<daysTilClosest:
        closestBirthday = birthday
        closestFriend = person
print (f"Closest birthday is {closestFriend}'s: " + closestBirthday.strftime("%m/%d/%Y"))