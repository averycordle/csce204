
def display_dictionary(items):
    for key in items:
        value = items[key]
        print(f"{key}: {value}")

def get_price(toys, toy):
    myToy = toy.strip().lower()

    if myToy in toys:
        return toys[myToy]
    else:
        return -1

def add_toy(toys, toyName, toyPrice):
    toys[toyName] = toyPrice
    return toys

toys = {
    "doll" : 10.99,
    "truck" : 5.60,
    "car" : 3.50,
    "book" : 7.20
}

display_dictionary(toys)

price = get_price(toys, "doll")
print(f"price is {price}")

toys = add_toy(toys, "bicycle", 49.99)
display_dictionary(toys)