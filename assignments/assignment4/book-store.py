#Author: Avery Cordle
#intro and prompt
print("***** Welcome to our bookstore *****")
path = input("What would you like to do (V)iew or (O)rder: ").lower().strip()

#if the user enters "v"
if path == "v":
    print(f"""Our catalogue consists of: 
- 1984 by George Orwell
- The Help by Kathryn Stockett
- Gone with the Wind by Margaret Mitchell
- The Fellowship of the Ring by J.R.R. Tolkien
""")

#if the user enters "o"
elif path == "o":
    buyBook = input("Enter book name: ").lower().strip()
    if buyBook == "1984":
        price = "9.99"
        print(f"You can buy {buyBook} for ${price}")
    elif buyBook == "the help":
        price = "7.59"
        print(f"You can buy {buyBook} for ${price}")
    elif buyBook == "gone with the wind":
        price = "8.50"
        print(f"You can buy {buyBook} for ${price}")
    elif buyBook == "fellowship of the ring":
        price = "10.11"
        print(f"You can buy {buyBook} for ${price}")
print("Have a nice day!")