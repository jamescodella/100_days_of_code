# Day 31: Flash card app

from tkinter import *
import pandas as pd
import random

# GLOBALS
BACKGROUND_COLOR = "#B1DDC6"
word_df = pd.read_csv('data/french_words.csv')
word_dict = word_df.to_dict(orient='records')
timer = None
word = None

def new_card(correct = False):
    '''
    Update card with new French word
    '''
    global word, timer
    
    window.after_cancel(timer)

    if correct == True:
        global score
        global word_dict
        word_dict.remove(word)
        pd.DataFrame(word_dict).to_csv('word_to_learn.csv')
    word =  random.choice(word_dict)
    card_canvas.itemconfig(card_image,image=card_front_image)
    card_canvas.itemconfig(language_label, text='French',fill="black",font="Arial 40 italic", anchor=CENTER)
    card_canvas.itemconfig(word_label, text=word['French'],fill="black",font="Arial 50 bold", anchor=CENTER)
    timer =  window.after(3000, flip_card)


def flip_card():
    '''
    Flip card over to reveal English
    '''
    global word
    card_canvas.itemconfig(card_image,image=card_back_image)
    card_canvas.itemconfig(language_label, text='English',fill="white",font="Arial 40 italic", anchor=CENTER)
    card_canvas.itemconfig(word_label, text=word['English'],fill="white",font="Arial 50 bold", anchor=CENTER)
    pass


window = Tk()
window.title('French 🇫🇷  Flashcard App')
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)

timer =  window.after(3000, flip_card)


# Card images and labels
card_back_image = PhotoImage(file='images/card_back.png')
card_front_image = PhotoImage(file='images/card_front.png')
card_canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0)
card_image = card_canvas.create_image(0, 0,image=card_front_image, anchor=NW)

language_label = card_canvas.create_text(400, 150, text='Title', fill="black",font="Arial 40 italic", anchor=CENTER)
word_label = card_canvas.create_text(400,264, text='Word', fill="black",font="Arial 50 bold", anchor=CENTER)
card_canvas.grid(column=0, columnspan=2, row=0, rowspan=1)

# Buttons
wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0,  borderwidth=0, command=lambda: new_card(correct = False))
wrong_button.grid(column=0, row=1)
right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0,  borderwidth=0, command=lambda : new_card(correct = True))
right_button.grid(column=1, row=1)

new_card()

window.mainloop()