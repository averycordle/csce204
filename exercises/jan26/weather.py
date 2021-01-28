#Author: Avery Cordle

print("What should you wear today?")

temp = float(input("Enter Temperature: "))
precip = input("Enter Percipitation (S)now (R)ain (N)one: ").lower().strip()

if temp <=32 and precip == "n":
    print("A Warm Jacket")
elif temp <=32 and precip == "s":
    print("A Snow Suit")
elif temp <=50 and precip == "n":
    print("A Jacket")
elif temp >=50 and precip == "r":
    print("A Rain Jacket")