#Author: Avery Cordle

class Bird:
    def __init__(self, bird_type, color, food, description):
        self.bird_type = bird_type
        self.color = color
        self.food = food
        self.description = description

    
    def is_match(self,bird_names):
        if self.bird_type==True:
            return False
        
        if bird_names == self.bird_type:
            return True
        return False

    def display(self):
        print(f"""
        *** {self.bird_type} ***
        Color: {self.color}
        Food: {self.food}
        {self.description}
        """)