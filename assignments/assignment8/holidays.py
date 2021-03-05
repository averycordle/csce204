#Author: Avery Cordle

from datetime import date, datetime, time

holidays = {
    "Valentine's Day": date(2021, 2, 14),
    "St. Patrick's Day": date(2021, 3, 17),
    "Easter": date(2021, 4, 4),
    "Mother's Day": date(2021, 5, 9),
    "4th of July": date(2021, 7, 4),
    "Halloween": date(2021, 10, 31),
    "Thanksgiving": date(2021, 11, 26),
    "Christmas": date(2021, 12, 25)
}

closestHoliday = date(2021, 12, 31)
holidayName = ""

for day in holidays:
    holiday = holidays[day]
    daysUntilClosest = (closestHoliday - date.today()).days
    daysUntilHoliday = (holiday - date.today()).days
    holidayName = day
    closestHoliday = holiday
    
    if daysUntilHoliday<0:
        print (f"{holidayName} - " + closestHoliday.strftime("%m/%d/%y") + " Passed")

    if daysUntilHoliday ==0:
        print (f"{holidayName} - " + closestHoliday.strftime("%m/%d/%y") + " TODAY!")

    if 1<daysUntilHoliday<30:
        print (f"{holidayName} - " + closestHoliday.strftime("%m/%d/%y") + f" only {daysUntilHoliday} days left")

    if daysUntilHoliday>30:
        print(f"{holidayName} - " + closestHoliday.strftime("%m/%d/%y"))