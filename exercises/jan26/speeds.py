#Author: Avery Cordle

print("Police Program")
print("You have been pulled over!")
speed = float(input("Enter speed: "))


if speed >= 100:
    print("Go to jail!")
elif speed >= 90:
    print("Big Ticket")
    ticketPrice = (speed - 70)*50
    print(f"Ticket price ${round(ticketPrice,2)}")
elif speed >= 80:
    print("Ticket")
    ticketPrice = (speed - 70)*20
    print(f"Ticket price ${round(ticketPrice,2)}")
elif speed >= 70:
    print("Warning")
elif speed >50:
    print("Good")
else:
    print("Too slow")



