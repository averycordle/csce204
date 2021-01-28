#Author: Avery Cordle

print("Let's find a Discount!")
weekDay = input("Enter week day: ").lower().strip()

if weekDay == "monday" or weekDay == "mon":
    print("Moes Monday")
elif weekDay == "tuesday" or weekDay == "tues":
    print("Taco Tuesday")
elif weekDay == "wednesday" or weekDay == "wed":
    print("Wicked Wednesday")
elif weekDay == "thursday" or weekDay == "thurs":
    print("Thirsty Thursday")
elif weekDay == "friday" or weekDay == "fri":
    print("Friendly Friday")
else:
    print("No discounts today")

print("Goodbye!")


