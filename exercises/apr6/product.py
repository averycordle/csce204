class Product: 
    def __init__(self,title,description,price):
        self.title = title
        self.description = description
        self.price = price

    def get_total_price(self):
        return self.price*1.07
        #tax

    def is_match(self,compare_title):
        if self.title.lower() == compare_title.lower():
            return True
        else:
            return False

    def display(self):
        print(f"""
            {self.title}
            Description: {self.description}
            Price: ${round(self.get_total_price(),2)}""")
