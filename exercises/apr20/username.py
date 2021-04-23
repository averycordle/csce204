import random
# email: jsmith@usc.edu, username: jsmith

def get_username(email):
    return email.split("@")[0]

def get_password(phrase):
    password = ""
    
    char_convers = {
        "a" : "@",
        "b" : "8",
        "e" : "3",
        "g" : "9",
        "i" : "!",
        "o" : "0",
        "s" : "$",
        "t" : "7"
    }

    for letter in phrase:
        l = letter.lower()
        if l in char_convers:
            password+= char_convers[l]
        else: 
            password += maybe_capitalize(l)
    return password + str(random.randint(0,100))

def maybe_capitalize(letter):
    if random.randint(0,2) == 0:
        return letter.lower()
    else:
        return letter.upper()

print("Username and Password Program")

email = input("Enter Email: ").strip()
username = get_username(email)
print(f"Email: {email}")
print(f"Username: {username}")

phrase = input("Enter phrase: ").strip()
password = get_password(phrase)
print(f"A good password would be: {password}")
