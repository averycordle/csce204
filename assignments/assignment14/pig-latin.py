#Author: Avery Cordle

def is_vowel(letter):
    let = letter[0]
    if let.lower() == "a" or let.lower() == "e" or let.lower() == "i" or let.lower() == "o" or let.lower() == "u":
        return True
    else: 
        return False

def convert_to_pig_latin(word):
    if is_vowel(word):
        print(f"{word} in pig-latin is {word}-hay")
    else:
        switch_consonant = word[0]
        final_word = ""
        for i in word:
            if i == word[0]:
                continue
            else:
                final_word+=i
        print(f"{word} in pig-latin is {final_word}-{switch_consonant}ay")

print("Welcome to Our Pig-Latin Translator!")
while True: 
    command = input("(C)onvert or (Q)uit: ").lower().strip()
    if command == "q":
        break
    elif command == "c":
        word = input("Enter a word: ")
        answer = convert_to_pig_latin(word)
    else: 
            print("Invalid Command")   

print("Goodbye")