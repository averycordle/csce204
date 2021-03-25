
toys = {
    "doll" : 10.99,
    "truck" : 5.60,
    "car" : 3.50,
    "book" : 7.20
}

toys["unicorn"] = 9.60

#loop through and display toys
for toy in toys:
    print(f"{toy}: ${toys[toy]}")

#ask for a toy and display the price
toyName = input("Enter toy name: ").strip().lower()

if toyName in toys:
    toyPrice = toys[toyName]
    print(f"{toyName}: ${toyPrice}")
else:
    print("Sorry, we don't have that toy")





