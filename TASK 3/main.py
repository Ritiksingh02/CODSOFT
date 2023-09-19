import random
import string
from tkinter import *
import pyperclip

def pass_gen():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    password_length = int(e2.get())
    selected_characters = ""

    if chk1_var.get():
        selected_characters += capital_alphabets
    if chk2_var.get():
        selected_characters += small_alphabets
    if chk3_var.get():
        selected_characters += numbers
    if chk4_var.get():
        selected_characters += special_characters

    if selected_characters:
        password = ''.join(random.sample(selected_characters, password_length))
        e1.delete(0, END)
        e1.insert(0, password)
    else:
        e1.delete(0, END)

def copy():
    random_pass = e1.get()
    pyperclip.copy(random_pass)

root = Tk()
root.geometry("275x280")
root.title("Password Generator")
root.config(bg="#151B54")

e1 = Entry(root, width=20, font="arial 16")
e1.place(x=15, y=30)
copybutton = PhotoImage(file="C:/Users/pc/Desktop/codsoft/copybutton.png")

button = Button(root, image=copybutton, bg="#FFFFFF", bd=0, command=copy)
button.image = copybutton  
button.place(x=233, y=31)

l1 = Label(root, text="Password Length", bg="#151B54", font="Times 10", fg="#FFFFFF")
l1.place(x=15, y=80)

e2 = Entry(root, width=8, font="arial 8")
e2.place(x=210, y=80)

l2 = Label(root, text="Include uppercase letters", bg="#151B54", font="Times 10", fg="#FFFFFF")
l2.place(x=15, y=110)

l3 = Label(root, text="Include lowercase letters", bg="#151B54", font="Times 10", fg="#FFFFFF")
l3.place(x=15, y=140)

l4 = Label(root, text="Include numbers", bg="#151B54", font="Times 10", fg="#FFFFFF")
l4.place(x=15, y=170)

l4 = Label(root, text="Include symbols", bg="#151B54", font="Times 10", fg="#FFFFFF")
l4.place(x=15, y=200)

button = Button(root, text="Generate Password", width=25, bg="#15317E", fg="#FFFFFF", font="Times 9", bd=0, padx=28, command=pass_gen)
button.place(x=15, y=230)

chk1_var = IntVar()
chk2_var = IntVar()
chk3_var = IntVar()
chk4_var = IntVar()

chk1 = Checkbutton(root, bg="#151B54", bd=0, fg="#151B54", variable=chk1_var)
chk1.place(x=245, y=110)

chk2 = Checkbutton(root, bg="#151B54", bd=0, fg="#151B54", variable=chk2_var)
chk2.place(x=245, y=140)

chk3 = Checkbutton(root, bg="#151B54", bd=0, fg="#151B54", variable=chk3_var)
chk3.place(x=245, y=170)

chk4 = Checkbutton(root, bg="#151B54", bd=0, fg="#151B54", variable=chk4_var)
chk4.place(x=245, y=200)

root.mainloop()
