#Author: Avery Cordle

print("Let's finish your room")
#gather the room details
roomWidth = float(input("Room Width: "))
roomLength = float(input("Room Length: "))
roomHeight = float(input("Room Height: "))

flooring = roomWidth * roomLength
ceiling = roomWidth * roomLength
drywall = roomWidth * roomLength + roomLength * roomHeight + roomWidth * roomHeight + roomLength * roomHeight + roomWidth * roomHeight

totalCost = flooring * 1.5 + ceiling * 0.5 + drywall * 2

print(f"Room finishing cost: ${totalCost}")
