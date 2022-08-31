from tkinter import Tk, Canvas, PhotoImage, Button, Label, Entry, messagebox
from random import randint, shuffle, choice
from json import dump, load
from pyperclip import copy

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_func():
    website = website_entry.get()
    u_name = u_name_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "u_name": u_name,
            "password": password,
        }
    }
    if website == "" or u_name == "" or password == "":
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty.")

    else:
        with open(file="data.json", mode="r") as file:
            data = load(file)
            data.update(new_data)

        with open(file="data.json", mode="w") as file:
            dump(data, file, indent=4)

        website_entry.delete(0, "end")
        password_entry.delete(0, "end")

    # else:
    #     is_ok = messagebox.askokcancel(title=website, message=f"Details entered: {u_name}\nPassword: {password}\nSave?")

    #     if is_ok:
    #         with open(file="password-list.txt", mode="a") as file:
    #             file.write(f"{website} | {u_name} | {password}\n")
    #         website_entry.delete(0, "end")
    #         password_entry.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

image = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)

canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", font=("Arial"))
website_label.grid(row=1, column=0)

website_entry = Entry(width=41)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

u_name_label = Label(text="Email/Username: ", font=("Arial"))
u_name_label.grid(row=2, column=0)

u_name_entry = Entry(width=41)
u_name_entry.grid(row=2, column=1, columnspan=2)
u_name_entry.insert(0, "filler_email@mail.com")

password_label = Label(text="Password: ", font=("Arial"))
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

gen_pass = Button(text="Generate Password", width=15, command=generate_password)
gen_pass.grid(row=3, column=2)

add_button = Button(text="Add", width=37, command=add_func)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
