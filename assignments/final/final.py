#Author: Avery Cordle
from man import Man

import turtle
import random

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()
style = ("Courier",20)

def start_game():
    word_options = []
    with open("assignments/final/words.txt") as file:
        for line in file:
            word_option = line.replace("\n", "").strip().lower()
            word_options.append(word_option)
        return word_options

def random_picker(options):
    the_word = random.choice(options)
    print(f"{the_word}")
    return the_word

def create_hypen(word):
    hypen_word = ""
    for i in range(len(word)):
        hypen_word+="_"
    return hypen_word

def display_word(word):
    display_word = " "
    pen.penup()
    pen.setpos(-150,150)
    pen.pendown()
    for i in range(len(word)):
        display_word+=word[i]+" "
    pen.write(display_word,font=style)

def check_word(word, letter):
    for i in word:
        if i.lower() == letter.lower():
            return True
    return False

def guess_letter(x,y):
    global the_word_chosen
    global guessed_word
    global wrong_attempt_number
    new_guessed_word = ""
    wrong_possibility = 0
    outcome=0
    letter = turtle.textinput("Letter Guessing", "Enter in a letter: ")
    #search for the letter in the word
    for i in range(len(the_word_chosen)):
        #replace the " " with the letter the user gave here
        if the_word_chosen[i] == letter:
            new_guessed_word+=letter
        #otherwise just add " " space
        else:
            new_guessed_word+=guessed_word[i]
    #here we check if the letter the usere guessed was in any of the mystery word
    for i in range(len(the_word_chosen)):
        #if the letter the user guessed was not a match for a letter in the mystery letter, add it to wrong_possibility
        if the_word_chosen[i] != letter:
            wrong_possibility+=1
        else:
            continue
    #if no correct letter was guessed, then wrong_possibility will = the length of the_word_chosen
    #this will cause the wrong_attempt_number to increase by one, and signal to draw another body part
    if wrong_possibility==len(the_word_chosen):
        wrong_attempt_number+=1
    guessed_word=new_guessed_word
    if new_guessed_word == the_word_chosen:
        outcome+=1
    display_word(guessed_word)
    #here we draw
    myMan= Man(50, wrong_attempt_number, outcome)
    myMan.draw(pen)

options = start_game()
the_word_chosen = random_picker(options)
guessed_word = create_hypen(the_word_chosen)
display_word(guessed_word)
x=0
y=0
wrong_attempt_number= 0

#click here to start
turtle.onscreenclick(guess_letter)

turtle.done()