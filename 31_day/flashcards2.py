from tkinter import *
from tkinter import messagebox
import random
import pandas
import json

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
TIMER = 3000

# ---------------------------- Read Header -----------------------------
try:
    with open("data/words_to_learn.csv") as file:
        language_header = file.readline()
        
except FileNotFoundError:
    with open("data/Oxford3000.csv") as file:
        language_header = file.readline()
finally:
    languages = language_header.rstrip('\n').split(',')
    
# ---------------------------- Read Data -------------------------------

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/Oxford3000_small.csv")      
finally:
    to_learn = data.to_dict(orient="records")
    
# data = pandas.read_csv("data/Oxford3000_small.csv")
# to_learn = data.to_dict(orient="records")

word = ""
translation = ""
LANGUAGES_ASK  = languages[0]      # e.g. English
LANGUAGES_ANSWER  = languages[1]   # e.g. German
front_side = True

# ---------------------------- Config -------------------------------
def pick_flashcard():
    global translation
    global flip_timer
    global front_side
    global current_card
    
    card_count = len(to_learn)
    
    if card_count:
        canvas.itemconfig(card_amount, text=f"Sum of flashcards: {card_count}.")
        current_card = random.choice(to_learn)
        word = current_card[LANGUAGES_ASK]
        translation = current_card[LANGUAGES_ANSWER]
            
        canvas.itemconfig(canvas_image, image=card_front_img)
        canvas.itemconfig(language_text, text=LANGUAGES_ASK, fill="black")    
        canvas.itemconfig(word_text, text=word, fill="black")
        front_side = True
            
        flip_timer = window.after(TIMER, flip_card)
    else:
        messagebox.showinfo(title="Finish", message="You have learned all flashcards!", icon="info")        

# ---------------------------- commands for buttons --------------------

def not_known():
    pick_flashcard()
    
def solved():
    to_learn.remove(current_card)
    
    data_learn  = pandas.DataFrame(to_learn)
    data_learn.to_csv("data/words_to_learn.csv", index=None)
        
    pick_flashcard()
    
# ---------------------------- Timer -----------------------------------
def flip_card():
    global translation
        
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(language_text, text=LANGUAGES_ANSWER, fill="white")    
    canvas.itemconfig(word_text, text=translation, fill="white")
  
# ---------------------------- Setup Screen ----------------------------

window = Tk()

window.title(f"Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(TIMER, flip_card)
canvas = Canvas(width=800, height=526)

# Ask-Image
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)

# Answer-Image
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_back_img)

language_text = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
card_amount = canvas.create_text(60, 520, text="", font=(FONT_NAME, 12, "italic"))
∫wrong_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_img, highlightthickness=0, command=not_known)
unknown_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=solved)
right_button.grid(row=1, column=1)
pick_flashcard()

window.mainloop()