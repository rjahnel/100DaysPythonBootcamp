from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import random
import pandas
import json

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
TIMER = 3000
BOXES = [0, 1, 2, 3, 4, 5]
timer_on = False
front_side = True
word = ""
translation = ""
actual_card_number = 0
actual_box_number = 0
sum_of_cards = 0

# ---------------------------- Config -------------------------------
def load_config():
    global timer_on
    
    init_config = {
        "Controlling": {
            "use_timer": True,
        }
    }
    
    try:
        with open('config.json', 'r') as config_file:
            # Reading old data
            config_data = json.load(config_file)
        
    except FileNotFoundError:
        with open('config.json', 'w') as config_file:
            #Create first entry
            json.dump(init_config, config_file, indent=4)
    else:
            if "Controlling" in config_data:
                timer_on = config_data["Controlling"]["use_timer"]
                
            config_file.close()

def pick_flashcard():
    global translation
    global flip_timer
    global front_side
    global current_card
    global actual_card_number
    global to_learn
    
    card_count = len(to_learn)
     
    if card_count:
        # get new card
        random.shuffle(to_learn)
        current_card = random.choice(to_learn)
        actual_card_number = to_learn.index(current_card)    
        word = current_card[LANGUAGES_ASK]
        translation = current_card[LANGUAGES_ANSWER]
        
        #debug
        #print(to_learn)
        #print(f"pick_flashcard(): Sum {card_count} ActNo: {actual_card_number} ActCard: {complete_data[actual_card_number]} Box {actual_box_number}")

        # setup card frontside
        canvas.itemconfig(canvas_image, image=card_front_img)
        canvas.itemconfig(language_text, text=LANGUAGES_ASK, fill="black")    
        canvas.itemconfig(word_text, text=word, fill="black")
        front_side = True

        # setup infor_line
        info_string = f"∑ {sum_of_cards} | "
        for i in range(len(BOXES)):
            info_string += f" [{i}]={len([card for card in complete_data if card['Box'] == i])} "

        canvas.itemconfig(card_amount, text=info_string)

        if timer_on:
            flip_timer = window.after(TIMER, flip_card)
    else:
        messagebox.showinfo(title="Finish", message="You have learned all flashcards in this box!", icon="info")

    
# ---------------------------- commands for buttons --------------------

def not_known():
    global to_learn
    global complete_data

    card_count = len(to_learn)
     
    if card_count and not front_side:
        if complete_data[actual_card_number]['Box'] > 0:
            complete_data[actual_card_number]['Box'] -= 1
        pick_flashcard()
    else:
        messagebox.showinfo(title="Finish", message="You have learned all flashcards in this box!", icon="info")

def solved():
    global to_learn
    global complete_data
    
    card_count = len(to_learn)
     
    if card_count and not front_side:
        # set card to next box
        
        # Find card in complete list, because of deleting items in der to_learn list (different indexes!!).
        complete_list_index = find(complete_data, LANGUAGES_ASK, current_card[LANGUAGES_ASK])
        
        if complete_data[complete_list_index]['Box'] < 5:
            complete_data[complete_list_index]['Box'] += 1

        # Only 5 boxes exists, after then the card can be removed
        if complete_data[complete_list_index]['Box'] == 5:
            complete_data.pop(complete_list_index)
              
        to_learn.pop(actual_card_number)

        #debug    
        # print(len(to_learn))
        # print(f"TO_LEARN: {to_learn}")
        # print(f"solved(): Sum {card_count} ActNo: {actual_card_number} ActCard: {to_learn[actual_card_number]} Box {actual_box_number}")

        pick_flashcard()
    else:
        messagebox.showinfo(title="Finish", message="You have learned all flashcards in this box!", icon="info")

def select_box(event):
    global to_learn
    global actual_box_number

    actual_box_number = int(event.widget.get())
    to_learn = [card for card in complete_data if card['Box'] == actual_box_number]
    pick_flashcard()

# ---------------------------- Timer -----------------------------------
def flip_card():
    global translation

    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(language_text, text=LANGUAGES_ANSWER, fill="black")    
    canvas.itemconfig(word_text, text=translation, fill="black")   
    
def flip(event=None): # After pressing Spacebar
    global front_side
    
    if not timer_on and front_side:
        front_side = False
        flip_card()
    
def next_solved(event=None): # After pressing Return
    if not timer_on and not front_side:
        solved()

def next_unknown(event=None): # After pressing Esc
    if not timer_on and not front_side:
        not_known()

# ---------------------------- Events ----------------------------------

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        data_learn = pandas.DataFrame(complete_data)
        data_learn.to_csv("data/cards_in_box.csv", index=None)
        window.destroy()

# ---------------------------- Helper ----------------------------------
def find(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1

# ============================ M A I N - P R O G R A M =================

# ---------------------------- Read Header -----------------------------
try:
    with open("data/cards_in_box.csv") as file:
        language_header = file.readline()
        
except FileNotFoundError:
    with open("data/vocabulary") as file:
        language_header = file.readline()
finally:
    languages = language_header.rstrip('\n').split(',')
    LANGUAGES_ASK  = languages[0]      # e.g. English
    LANGUAGES_ANSWER  = languages[1]   # e.g. German
    
# ---------------------- Read Data from box 0 -------------------------
try:
    data = pandas.read_csv("data/cards_in_box.csv")

except FileNotFoundError:
    data = pandas.read_csv("data/vocabulary.csv")      

finally:
    complete_data = data.to_dict(orient="records")
    to_learn = [card for card in complete_data if card['Box'] == 0]   # set box 0 to default box
    card_count = len(to_learn)
    
# ---------------------------- Setup Screen ----------------------------

window = Tk()
load_config()

window.title(f"Flashcards : Timer is {'on' if timer_on else 'off - use <spacebar> to flip card - <return> for known - <esc> for not known.'}")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

if timer_on:
    flip_timer = window.after(TIMER, flip_card)

canvas = Canvas(width=800, height=526)

# Ask-Image
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)

# Answer-Image
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_back_img)

language_text = canvas.create_text(400, 75, text="", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=0, columnspan=2)

card_amount = canvas.create_text(170, 493, text="", font=(FONT_NAME, 10, "bold"), fill='green')
Button(window, text = '', command = next_solved)
Button(window, text = '', command = next_unknown)

# create a combobox
selected_box = StringVar()
learn_box_label = Label(window, text="Select Learnbox: ", bg=BACKGROUND_COLOR, font=(FONT_NAME, 12, "bold"))

learn_box = Combobox(window, textvariable=selected_box)
learn_box['values'] = BOXES
learn_box['state'] = 'readonly' # prevent typing a value
learn_box.current(0)
learn_box_label.grid(row=0, column=0, columnspan=2)
learn_box.grid(row=0, column=1, columnspan=2)

window.bind('<space>', flip)
window.bind('<Return>', next_solved)
window.bind('<Escape>', next_unknown)
learn_box.bind("<<ComboboxSelected>>", select_box)
window.protocol("WM_DELETE_WINDOW", on_closing) # on_closing_window action

wrong_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_img, highlightthickness=0, command=not_known)
unknown_button.grid(row=2, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=solved)
right_button.grid(row=2, column=1)
sum_of_cards = len(complete_data)

pick_flashcard()
window.mainloop()
