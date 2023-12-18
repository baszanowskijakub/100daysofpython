from tkinter import *


def button_clicked():
    new_text = round(int(input_entry.get()) * 1.609)
    label3.config(text=f"{new_text}")



window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=50)
window.config(padx=20, pady=20)


input_entry = Entry(width=10)
input_entry.grid(column=2, row=0)

label1 = Label(text="Miles")
label1.grid(column=3, row=0)

label2 = Label(text="is equal to")
label2.grid(column=1, row=1)

label3 = Label(text=f"0")
label3.grid(column=2, row=1)

label4 = Label(text="Km")
label4.grid(column=3, row=1)

value_in_m = 0

button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=2)


window.mainloop()