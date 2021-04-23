def replace_stars():
    global word

    answer = ""

    for letter in word:
        if letter == "*":
            answer+="."
        else:
            answer+=letter


    word = answer




word = "a*b*c*d*e"
replace_stars()
print(word)