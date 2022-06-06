# ---------------------------- Pomodoro App ---------------------------- #

from tkinter import *
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
SECONDS = 60
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1    
    
    work_sec = WORK_MIN * SECONDS
    short_break_sec = SHORT_BREAK_MIN * SECONDS
    long_break_sec = LONG_BREAK_MIN * SECONDS
    
            
    if reps % 8 == 0:    
        count_down(long_break_sec)
        timer_label.config(text = "Break", fg=RED)
        
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text = "Break", fg=PINK)
        
    else:
        count_down(work_sec)
        timer_label.config(text = "Work", fg=GREEN)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minutes = math.floor(count / SECONDS)
    count_seconds = count % SECONDS
    
    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"
        
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        work_sessions = math.floor(reps/2)
        check_txt = "✓" * (work_sessions + 1)
        check_marks.config(text=check_txt)            
        start_timer()

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


timer_button = Button(text="Start", highlightthickness=0, command=start_timer)
timer_button.grid(column=0, row=2)

reset_timer = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_timer.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30,"bold"))
check_marks.grid(column=1, row=3)


window.mainloop()