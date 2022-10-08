from tkinter import *
from tkinter import messagebox
import pyperclip
import json
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

    # password = ""
    #
    # for char in password_list:
    #   password += char

    password = "".join(password_list)

    entry_pass.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web_name = entry_web.get()
    account = web_entry.get()
    pass_word = entry_pass.get()
    new_data = {
        web_name: {
            "email": account,
            "password": pass_word,
        }
    }


    if len(web_name) == 0 or len(pass_word) == 0:
        messagebox.showinfo(title="Oops", message=f"please fill the empty column before adding it.")
    else:
        # is_ok = messagebox.askyesnocancel(title=web_name, message=f"There are the details entered : \nEmail:{account}"
        #                                                        f"\nPassword:{pass_word}\n Is it Ok to Save?")

        # while is_ok:
        try:
            with open("file.json", "r") as opening:
                data = json.load(opening)
        except FileNotFoundError:

            with open("file.json", "w") as opening:
                json.dump(new_data, opening,indent=4)

        else:
            data.update(new_data)
            with open("file.json", "w") as opening:
                json.dump(new_data, opening, indent=4)
        finally:
                web_entry.delete(0, END)
                entry_pass.delete(0, END)
# ---------------------------- find password ------------------------------- #
def find_password():
    website = web_entry.get()
    try:
        with open("file.json") as opening:
            data = json.load(opening)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="no data File found.")
    else:
        if website in data :
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Emails:{email}\nPassword : {password}")
        else:
            messagebox.showinfo(title="Error",message= f"no details for {website} exists.")



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
search_button = Button(text="Search",width=13)
search_button.grid(row=1, column=2)

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


