from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R","S", "T", "U", "V",
            "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n","o", "p", "q", "r",
            "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "$", "%", "#", "()", ")", "%", "#"]

    n_letters = random.randint(8, 10)
    n_numbers = random.randint(2, 4)
    n_symbols = random.randint(2, 4)

    l_password = []
    l_password += [random.choice(letters) for _ in range(n_letters)]
    l_password += [random.choice(numbers) for _ in range(n_numbers)]
    l_password += [random.choice(symbols) for _ in range(n_symbols)]

    random.shuffle(l_password)
    pass_word = ""
    pass_word = "".join(l_password)
    password.delete(0, END)
    password.insert(0, pass_word)
    
    # copy to clipboard
    window.clipboard_clear()
    window.clipboard_append(pass_word)
    window.update() # stays on the clipboard after the window is closed
        
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_account():
    var_website = website.get()
    var_username = username.get()
    var_password = password.get()
    
    if not var_website or not var_username or not var_password:
        messagebox.showinfo(title="Ooops", message="Please don't leave any field empty!", icon="warning")
    elif messagebox.askyesno(title=var_website, message=f"These are the details entered: \nusername:{var_username} "
                                              f"\nPassword: {var_password} \nIs it ok to save?", icon="question"):
        with open('data.txt', 'a') as file:
            file.write(f"{var_website} | {var_username} | {var_password}\n")
            file.close()
        messagebox.showinfo(title="Password Manager", message="Password is saved", icon="info")
        website.delete(0, END)
        password.delete(0, END)
        website.focus_set()
        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Username/Password:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entrys
website = Entry(width=39)
website.grid(column=1, row=1, columnspan=2)
username = Entry(width=39)
username.grid(column=1, row=2, columnspan=2)
password = Entry(width=21)
password.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=37, command=save_account)
add_button.grid(column=1, row=4, columnspan=2)

website.focus_set()
username.insert(0, "coder@coding.com")

window.mainloop()