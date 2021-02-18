#Author: Avery Cordle

weekDays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

#loop through and display items in the tuple

#for day in weekDays:
    #print(day, end="")
    #end="" means there will be no ending character to print on a new line

counter = 0
for day in weekDays:
    if counter == len(weekDays)-1:
        print(f"{day} ")
    else:
        print(f"{day}, ", end="")
    
    counter += 1
