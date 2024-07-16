from tkinter import *
import string
import random
import pyperclip
def generate_password():
    lowercase_alphabets = string.ascii_lowercase
    uppercase_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation
    combination_of_characters = lowercase_alphabets+uppercase_alphabets+numbers+special_characters
    password_length = int(length_box.get())
    if choice.get() == 1:
        generated_password.insert(0, random.sample(lowercase_alphabets, password_length))
    elif choice.get() == 2:
        generated_password.insert(0, random.sample(lowercase_alphabets+numbers+uppercase_alphabets, password_length))
    elif choice.get() == 3:
        generated_password.insert(0, random.sample(combination_of_characters, password_length))

def copy_password():
    copy_pass = generated_password.get()
    pyperclip.copy(copy_pass)

base = Tk()

base.title("Password Generator")
base.config(bg="SlateBlue4")
base.geometry("500x500")

choice = IntVar()

font_style = ('Lucida Grande', '16', 'bold')

password_title = Label(base, text="Password Generator", font=('Lucida Grande', 25, 'bold'), bg='SlateBlue4', fg='white')

password_title.grid(pady=15)

choice_selection = Label(base, text="Enter the password type of your choice", font=('Lucida Grande',20,'bold'), fg='white', bg='SlateBlue4')
choice_selection.grid(pady=5)

weak_button = Radiobutton(base, text="Weak", value=1, variable=choice, font=font_style, bg='SlateBlue4', fg='white')
weak_button.grid(pady=5)

medium_button = Radiobutton(base, text="Medium", value=2, variable=choice, font=font_style, bg='SlateBlue4', fg='white')
medium_button.grid(pady=5)

strong_button = Radiobutton(base, text="Strong", value=3, variable=choice, font=font_style, bg='SlateBlue4', fg='white')
strong_button.grid(pady=5)

length_label = Label(base, text="Enter the password length of your choice", font=('Lucida Grande', 20, 'bold'), bg='SlateBlue4', fg='white')
length_label.grid(pady=5)

length_box = Spinbox(base, from_=4, to=20, width=5, font=font_style,bg='white',fg='gray1')
length_box.grid(pady=5)

generate_button = Button(base, text="Generate Password", font=font_style, command=generate_password)
generate_button.grid(pady=5)

generated_password = Entry(base, width=30,bd=3,bg='white', fg='gray1')
generated_password.grid(pady=5)

copy_button = Button(base, text="Copy Password", font=font_style, command=copy_password)
copy_button.grid(pady=5)

base.mainloop()
