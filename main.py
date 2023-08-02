import tkinter
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyAesCrypt
import os
import pyperclip
import tkinter.simpledialog

password = "this_is_a_long_password"



def encrypt():
    # encrypt
    pyAesCrypt.encryptFile("data.txt", "data.txt.aes", password)


def decrypt():
    # decrypt
    try:
        pyAesCrypt.decryptFile("data.txt.aes", "dataout.txt", password)
        with open('dataout.txt', 'r') as firstfile, open('data.txt', 'w') as secondfile:
            # read content from first file
            for line in firstfile:
                # append content to second file
                secondfile.write(line)
    except:
        ValueError
    else:
        pass


decrypt()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    '''In this list comprehension we create random letters for password'''
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)

    password_generate = "".join(password_list)
    """Here we are printing password to the password entry"""
    reset_pass()
    line_4_password.insert(0, password_generate)
    pyperclip.copy(password_generate)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    text_website = website.get()
    text_password = passwordz.get()
    text_username = email.get()

    if len(website.get()) == 0 or len(passwordz.get()) == 0:
        messagebox.showinfo(title="Oops", message=f"Please make sure that you haven't left any field empty.")
    else:

        is_ok = messagebox.askokcancel(title=text_website,
                                       message=f"These are the details entered: \nWebsite: {text_website}"
                                               f"\nEmail: {text_username} \nPassword:"
                                               f"{text_password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{text_website} | {text_username} | {text_password} \n")
                reset()


# ws = Tk()


def save_exit():
    """Here we will encrypt all files that have been entered during work with program"""
    encrypt()  # encrypt files
    os.remove("data.txt")  # remove txt file
    try:
        os.remove("dataout.txt")
    except:
        FileNotFoundError
    else:
        pass
    window.destroy()
    window.quit()


def reset():
    website.set("")
    passwordz.set("")


def reset_pass():
    passwordz.set("")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=350, height=350, background="White")

my_img = PhotoImage(file='logo.png')
line_1 = Label(image=my_img)
line_1.grid(row=0, column=1)

# Labels
line_2_text = Label(text="Website:")
line_2_text.grid(row=2, column=0)
line_3_text = Label(text="Email/Username:")
line_3_text.grid(row=3, column=0)
line_4_text = Label(text="Password:")
line_4_text.grid(row=4, column=0)

# Entry

website = StringVar()
email = StringVar()
passwordz = StringVar()
line_2_website = Entry(master=None, width=38, textvariable=website)
line_2_website.grid(row=2, column=1, columnspan=2)
line_2_website.focus()
line_3_email = Entry(width=38, textvariable=email)
line_3_email.grid(row=3, column=1, columnspan=2)
line_3_email.insert(0, "dmoharic@gmail.com")
line_4_password = Entry(width=21, textvariable=passwordz)
line_4_password.grid(row=4, column=1)

# Buttons
line_4_button_password = Button(text="Generate Password", command=generate_password)
line_4_button_password.grid(row=4, column=2)
line_5_button_add = Button(text="Add", width=36, command=save)
line_5_button_add.option_clear()
line_5_button_add.grid(row=5, column=1, columnspan=2)
line_6_button_save = Button(text="Save & exit", width=36, command=save_exit)
line_6_button_save.grid(row=6, column=1, columnspan=2)

window.mainloop()
