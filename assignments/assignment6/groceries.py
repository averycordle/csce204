#Author: Avery Cordle

groceries = ["bananas", "blueberries", "avocados", "cherries", "tomatoes"]

print(f"""
Welcome to our grocery store
The following items are in the store:
""")

for grocery in groceries:
    print(grocery)

order = input("What would you like to order? ").lower().strip()

if order in groceries:
    print(f"We've ordered {order} for you")
    groceries.remove(order)
    print("Now the grocery store contains the following: ")
    for grocery in groceries:
        print(grocery)
else: 
    print(f"Sorry, we don't have any {order}")
    print("Now the grocery store contains the following: ")
    for grocery in groceries:
        print(grocery)
    
print("Goodbye")