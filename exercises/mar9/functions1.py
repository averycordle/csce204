#Author: Avery Cordle
"""
#march 9th work:
def say_hello():
    print("hello world")
    print("have a great day!")
def say_goodbye():
    print("Bye!")

say_hello()
say_goodbye()
say_hello()
say_hello()
"""

def say_hello(firstName, lastName):
    print(f"Hello, {firstName} {lastName}")
def say_goodbye(firstName, lastName):
    print(f"Goodbye, {firstName} {lastName}")

print("My Simple Program")
userFirstName = input("Enter your name: ")
userLastName = input("Enter your last name: ")
say_hello(userFirstName, userLastName)
print("Have a great day!")
say_goodbye(userFirstName, userLastName)



