def get_phone_numbers():
    phoneBook = {}

#loop through the file and add each line as an entry in the phone book
    with open("mar23/phones.txt") as file:
        for line in file:
            #split based on the comma 
            data = line.split(',') #data is now an array
            friendName = data[0].strip()#gets the name in the 0 postion
            phone = data[1].strip()#gets the phone number in the 1 position #gets rid of the space infront of the phone number
            phoneBook[friendName] = phone

    return phoneBook

#given a dictionary of phone numbers, display them

def display_phone_numbers(phoneBook):
    for person in phoneBook:
        phone = phoneBook[person]
        print(f"{person}: {phone}")

def getPhoneNumber(phoneBook):
    friend = input("Enter name: ").strip().lower()
    if friend in phoneBook:
        return phoneBook [friend]
    else:
        return -1 #-1 means error

phoneBook = get_phone_numbers()
display_phone_numbers(phoneBook)
phoneNum = getPhoneNumber(phoneBook)

if phoneNum == -1:
    print("Sorry, we don't have that phone number")
else:
    print(f"Phone Number is {phoneNum}")