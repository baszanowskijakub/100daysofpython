from tkinter import *

import pandas
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Getting French word from the french_words.csv
try:
    data = read_csv("data\\words_to_learn.csv")
except FileNotFoundError:
    original_data = read_csv("data\\french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# Function that picks a random French word
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(current_image, image=french_side)
    flip_timer = window.after(3000, flip_card)


# Function that flips the current card
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(current_image, image=english_side)


# Function that removes the known card from the list after clicking a tick
def remove_word():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data\\words_to_learn.csv", index=False)


# Main window
window = Tk()
window.title("Flashy")
window.config(width=800, height=526, pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

# Create and configure canvas
canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR)
french_side = PhotoImage(file="images/card_front.png")
english_side = PhotoImage(file="images/card_back.png")
current_image = canvas.create_image(400, 263, image=french_side)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, columnspan=2, row=0)

# Buttons
tick_image = PhotoImage(file="images/right.png")
tick = Button(image=tick_image, highlightthickness=0, command=remove_word)
tick.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong.grid(column=0, row=1)

next_card()
window.mainloop()