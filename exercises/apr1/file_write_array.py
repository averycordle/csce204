friends = ["Sarah", "Sam", "Abbi", "Rachel"]

with open("friends.txt", "w") as file:
    for friend in friends:
        file.write(f"{friend}\n")
        print(friend)