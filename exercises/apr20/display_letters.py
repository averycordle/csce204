#first easy example
"""
def display_letters(word):
    for i in range(len(word)):
        print(word[i])

display_letters("Welcome")
"""
"""
def display_star_word(word):
    print("*", end="")
    for i in range(len(word)):
        print(word[i] + "*", end="")#this will make the word go sraight across
    print()

display_star_word("Welcome")
"""

def in_word(word, letter):
    for i in word:
        if i.lower() == letter.lower():
            return True
    return False

if in_word("welcome", "c"):
    print("Yay!")
else:
    print("Nay!")










