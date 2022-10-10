from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
from random import choice, randint, shuffle

def generate_pass():
    entry_pass.delete(0,20)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
               'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_list = []


    password_letters = [(choice(letters)) for char in range(randint(8, 10))]


    password_symbols = [choice(symbols) for char in range(randint(2, 4))]


    password_numbers = [choice(numbers) for char in range(randint(2, 4))]
    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)


    password = "".join(password_list)

    entry_pass.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = entry_web.get()
    email = web_entry.get()
    password = entry_pass.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("file.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                entry_web.delete(0, END)
                entry_pass.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("password-manager")

canvas = Canvas(width=200, height=200)
window.config(padx=20,pady=20)

image_pass = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_pass)
canvas.grid(column=1,row=0)

web_label = Label(text="Website :")

web_label.grid(column=0,row=1)
entry_web = Entry(width=50)
entry_web.focus()

entry_web.grid(column=1,row=1,columnspan=2)

web_label = Label(text="Email/Username :")

web_label.grid(column=0,row=2)
web_entry = Entry(width=50)
web_entry.insert(0, "rohan@gmail.com")
web_entry.grid(column=1,row=2,columnspan=2)

web_label = Label(text="Password :")
web_label.grid(column=0,row=3)
entry_pass = Entry(width=32)

entry_pass.grid(column=1,row=3)

button = Button(text="Generate Password",width=14,command=generate_pass)

button.grid(column=2,row=3)

button = Button(text="Add",width=42,command=save)
button.grid(column=1,row=4,columnspan=2,pady=10)


window.mainloop()


