from tkinter import *
from turtle import window_width
from tkinter import messagebox
import string
import random
import pyperclip
import json

STARTING_EMAIL = 'test@email.com'

def generate_random_password():
    '''
    Generates random password using letters, numbers, and punctuation symbols, then copies it to the clipboard and password entry field 
    Min length = 12, max length = 18
    '''
    letters = [random.choice(string.ascii_letters) for _ in range(random.randint(8,10))]
    numbers = [random.choice(string.digits) for _ in range(random.randint(2,4))]
    punctuations = [random.choice(string.punctuation) for _ in range(random.randint(2,4))]

    password = letters + numbers + punctuations
    random.shuffle(password)
    password = ''.join(password)
    password_entry.insert(0,password)
    pyperclip.copy(password)

def add_password():
    '''
    Adds the website, info, and password to the local data.txt file
    '''
    website = website_entry.get()
    info = info_entry.get()
    password = password_entry.get()

    if website == '' or info == '' or password == '':
        messagebox.showerror(title=website, message='Please make sure none of the fields are empty!')
    else:
        ok_to_save = messagebox.askokcancel(title=website, message=f'Is the information you entered correct?\Info: {info}\nPassword: {password}\n OK to save?')

        if ok_to_save:
            to_save =','.join([website_entry.get(), info_entry.get(), password_entry.get()])
            with open('data.txt', 'a+') as file:
                file.write(to_save+'\n')
            website_entry.delete(0,END)
            password_entry.delete(0,END)


window = Tk()
window.config(padx=50, pady=50)

window.title('Password Manager 🔐')

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

info_label = Label(text='Email/Username:')
info_label.grid(row=2, column=0)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Entry fields
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1,columnspan=2)
website_entry.focus()

info_entry = Entry(width=35)
info_entry.grid(row=2, column=1,columnspan=2)
info_entry.insert(0,STARTING_EMAIL)

password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = Button(text='Generate Password', command=generate_random_password)
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', width=34, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()