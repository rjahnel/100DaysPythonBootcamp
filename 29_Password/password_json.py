from tkinter import *
from tkinter import messagebox
import random
import json
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
    
    new_data = {
        var_website: {
            "user": var_username,
            "password": var_password,
        }
    }
    
    if not var_website or not var_username or not var_password:
        messagebox.showinfo(title="Error", message="Please don't leave any field empty!", icon="warning")
    elif messagebox.askyesno(title=var_website, message=f"These are the details entered: \nusername:{var_username} "
                                              f"\nPassword: {var_password} \nIs it ok to save?", icon="question"):
        
        try:
            with open('data.json', 'r') as file:
                # Reading old data
                data = json.load(file)
        
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                #Create first entry
                json.dump(new_data, file, indent=4)
        else:
            #updateing old data with new data
            data.update(new_data)
                            
            with open('data.json', 'w') as file:
                #Saving updated data
                json.dump(data, file, indent=4)
                file.close()
        
        finally:    
            messagebox.showinfo(title="Password Manager", message="Password is saved", icon="info")
            website.delete(0, END)
            password.delete(0, END)
            window.focus_set()
            website.focus_set()

# ---------------------------- Lookup data ---------------------------- #     
def search_data():
    try:
        with open('data.json') as file:
            # Reading old data
            data = json.load(file)
            
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File data.json not found", icon="warning")
    else:
        wsite = website.get()
        if wsite in data:
            messagebox.showinfo(title=wsite, message=f"Username: {data[wsite]['user']}\nPassword: {data[wsite]['password']}", icon="info")
        else:
            messagebox.showinfo(title="Error", message=f"No entry for website: {wsite} found!", icon="warning")
    
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
username_label = Label(text="Username/Email:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entrys
website = Entry(width=21)
website.grid(column=1, row=1)
username = Entry(width=39)
username.grid(column=1, row=2, columnspan=2)
password = Entry(width=21)
password.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=37, command=save_account)
add_button.grid(column=1, row=4, columnspan=2)

add_button = Button(text="search", width=13, command=search_data)
add_button.grid(column=2, row=1)

website.focus_set()
username.insert(0, "coder@coding.com")

window.mainloop()