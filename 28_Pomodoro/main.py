from audioop import tomono
import imp
from tkinter import *
from tracemalloc import start
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    
    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"
        
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#CONTROLS
timer_label = Label(text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_timer = Button(text="Start", highlightthickness=0, command=start_timer)
start_timer.grid(column=0, row=2)

reset_timer = Button(text="Reset", highlightthickness=0)
reset_timer.grid(column=2, row=2)

check_marks = Label(text="✓",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30,"bold"))
check_marks.grid(column=1, row=3)


window.mainloop()