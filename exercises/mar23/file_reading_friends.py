"""
with open ("mar23/friends.txt") as file:
    for line in file:
        print(line, end="")
"""

#create an array of friends from the file
def get_friends():
    friends = []
    #populate array with friends from file
    with open ("mar23/friends.txt") as file:
        for line in file:
            friend = line.replace("\n","")
            friends.append(friend)

    return friends

#get friends, loop through and display them
chums = get_friends()
print("My best friends!")

#loop through and display list of friends in format: 1.Sarah
for i in range(len(chums)):
    print(f"{i+1}. {chums[i]}")