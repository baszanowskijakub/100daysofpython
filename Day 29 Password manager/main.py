from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, height=200, width=200)
canvas = Canvas(window, width=200, height=200)
canvas.grid(column=1, row=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    random_password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    login = login_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="You left one of the fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nLogin/Email: {login} \n"
                                                      f"Password: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as passwords:
                entry = f"{website} | {login} | {password} \n"
                passwords.write(entry)
                password_entry.delete(0, "end")
                website_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

login_label = Label(text="Email/Username:")
login_label.grid(column=0, row=2)

login_entry = Entry(width=35)
login_entry.grid(column=1, row=2, columnspan=2)
login_entry.insert(0, "baszanowskijakub@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=3, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
