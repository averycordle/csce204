#ask the user to enter a price, if they enter a valid float return it 
#if they enter an invalid float, give them feedback and keep looping
def getPrice():
    while True:
        try:
            price = float(input("Enter Price: "))
            if price>=0:
                return price
            else:
                print("You must enter a number greater than 0")
        except ValueError:
            print("Sorry, that is not a valid number.")

#ask the user to enter a quantity, if they enter a valid int, retun it
#if they enter an invalid int, give them feeback and keep looping
def getQuantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity>=0:
                return quantity
            else:
                print("You must enter a number greater than 0")
        except ValueError:
            print("Sorry, that is not a valid whole number.")

print("Our cost calculator")
price = getPrice()
quantity = getQuantity()
total = quantity*price*1.07
print(f"The price is ${round(total,2)}")