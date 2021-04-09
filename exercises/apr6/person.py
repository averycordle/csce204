class Person:
    #classes are often thought of as blueprints
    #first we will make a constructor
    def __init__(self,first_name,last_name,phone_number):
        #methods are functions inside objects
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        #this is now a container that holds this information

    def display(self):
        print(f"Hello {self.first_name} {self.last_name}: {self.phone_number}")