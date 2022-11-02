from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website_string = website_entry.get()
    email_string = email_entry.get()
    password_string = password_entry.get()
    f = open("credentials.txt", "a")
    credentials = (website_string + "|" + email_string + "|" + password_string + "\n")
    f.write(credentials)
    f.close()
    website_entry.delete(0, END)
    email_entry.delete(0,END)
    password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label =  Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="email/User")
email_label.grid(row=2, column=0)
password_label = Label(text="password")
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus() # set the cursor in that field
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"peterwallner_@hotmail.com") # prefill the email field
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_passw_button = Button(text="Generate password")
generate_passw_button.grid(row=3, column=2)
add_button = Button(text="add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)



mainloop()