from tkinter import *

def calc_amout_of_oil():
    oil_amount = (float(number_of_tanks.get()) * float(max_tank_filling.get()) * float(oil_level.get())) / float(tank_height.get())
    remaining_capa.insert(END, string=str(round(oil_amount,2)))
    oil_level.focus()
    
 
#Creating a new window and configurations
window = Tk()
window.title("TankCalc")
window.config(padx=20, pady=20)

#Controls
oil_level = Entry(width=7, bg='yellow')
oil_level.grid(column=1, row=0)
oil_level_label = Label(text="Oil level in meter", width=20, anchor='w')
oil_level_label.grid(column=0, row=0)

number_of_tanks = Entry(width=7)
number_of_tanks.grid(column=1, row=1)
number_of_tanks.insert(END, string="5")
number_of_tanks_label = Label(text="Number of tanks", width=20, anchor='w')
number_of_tanks_label.grid(column=0, row=1)

max_tank_filling = Entry(width=7)
max_tank_filling.grid(column=1, row=2)
max_tank_filling.insert(END, string="2000")
max_tank_filling_label = Label(text="Max. tank filling", width=20, anchor='w')
max_tank_filling_label.grid(column=0, row=2)

tank_height = Entry(width=7)
tank_height.grid(column=1, row=3)
tank_height.insert(END, string="1.5")
tank_height_label = Label(text="Tank hight", width=20, anchor='w')
tank_height_label.grid(column=0, row=3)

remaining_capa = Entry(width=7, bg='lightgreen')
remaining_capa.grid(column=1, row=4)
remaining_capa_label = Label(text="Remaining capacity in litres", width=20, anchor='w')
remaining_capa_label.grid(column=0, row=4)

calculate_button = Button(text="Calculate", command=calc_amout_of_oil)
calculate_button.grid(column=1, row=6)

window.mainloop()