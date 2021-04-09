from person import Person
#longer directory path if you need it: april8.person

friend = Person("Amy","Smith","123-456-7890")
enemy = Person("Brad","Jinkins","123-456-7899")

friend.display()

"""
print(f"{enemy.first_name} {enemy.last_name}: {enemy.phone_number}")
"""
people = (
    Person("Kim","White","803-554-6645"),
    Person("Bobby","Smith","803-789-8225"),
    Person("Sam","Anderson","803-44-3343")
)

for person in people:
    person.display()