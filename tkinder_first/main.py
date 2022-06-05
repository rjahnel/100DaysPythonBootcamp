from  tkinter import *


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


# Label
my_label = Label(text="Input text and click button", font=("Arial", 24, "bold"))
my_label.pack()

# Entry
input = Entry(width=40)
input.pack()

# Button
button = Button(text="Save", command=button_clicked)
button.pack()



window.mainloop()
