from product import Product

#create a list of products
def display_products(products):
    for product in shopping_list:
        product.display()

def get_total_cost(products):
    total = 0
    for product in shopping_list:
        total+=product.get_total_price()
    
    return total

def get_product_details(products,title):
    for product in products:
        if product.is_match(title):
            product.display()
            return

shopping_list = (
    Product("Lipstick","Red",15.99),
    Product("Eyeshadow","Neutrals, tans, browns, and blacks",49.99),
    Product("Foundation","Skin Tone",35.99)
)

while True:
    command = input("Enter (L)ist, (D)isplay, (T)otal, or (Q)uit: ").strip().lower()

    if command == "q":
        break
    elif command == "l":
        display_products(shopping_list)
    elif command == "d":
        productName = input("Enter product name: ").lower().strip()
        get_product_details(shopping_list, productName)
    elif command == "t":
        cost = get_total_cost(shopping_list)
        print(f"Your order total is: $ {round(cost,2)}")
    else:
        print("Invalid Command")