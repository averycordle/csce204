#Author: Avery Cordle
"""
def get_mood(color):
    mycolor = color.lower().strip()

    if color == "red":
        return "angry"
    elif color == "yellow":
        return "mellow"
    elif color == "blue":
        return "sad"
    elif color == "green":
        return "happy"
    elif color == "black":
        return "scary"
    elif color == "purple":
        return "royal"
    elif color == "pink":
        return "fun"
    else:
        return False
"""

def get_mood(color):
    color_moods = {
        "red":"angry",
        "yellow":"mellow",
        "blue":"sad",
        "green":"happy",
        "black":"scary",
        "purple":"royal",
        "pink":"fun"
    }
    if color in color_moods:
        return color_moods[color]
    else:
        return False

userInput = input("pick a color: ").lower().strip()
myMood = get_mood(userInput)

if (myMood != False):
    print(f"You are feeling very {myMood}")
else:
    print("Sorry, invalid color")




"""
colors = ("red","yellow","blue","green","black","purple","pink")
mood = ("angry","mellow","sad","happy","scary","royal","fun")
"""






