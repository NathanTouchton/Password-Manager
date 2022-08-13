from tkinter import Tk, Canvas, PhotoImage, Button, Label, Entry

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_func():
    with open(file="password-list.txt", mode="a") as file:
        file.write(f"{website_entry.get()} | {u_name_entry.get()} | {password_entry.get()}\n")

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

gen_pass = Button(text="Generate Password", width=15)
gen_pass.grid(row=3, column=2)

add_button = Button(text="Add", width=37, command=add_func)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
