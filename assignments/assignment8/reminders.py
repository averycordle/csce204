#Author: Avery Cordle

from datetime import date, datetime, time

reminders = {
    "1. Wake-up - 7:30 AM": time(7,30),
    "2. Exercise - 8:15 AM": time(8,15),
    "3. Shower - 10:00 AM": time(10,00),
    "4. Breakfast - 10:30 AM": time(10,30),
    "5. Work - 11:30 AM": time(11,30),
    "6. Lunch - 2:00 PM": time(14,00),
    "7. Work - 2:30 PM": time(14,30),
    "8. Dinner - 5:00 PM": time(17,00),
    "9. Work - 7:00 PM": time(19,00),
    "10. Relax and Get Ready for Bed - 9:30 PM": time(21,30),
    "11. Go to Sleep - 10:30 PM": time(22,30)
}

for reminder in reminders:
    print(reminder)