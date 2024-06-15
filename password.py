import tkinter as tk
from tkinter import StringVar, IntVar, Checkbutton
import random
import string

def generate_password(length, use_special_chars):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
def display_password():
    length = length_var.get()
    use_special_chars = special_chars_var.get()
    pwd = generate_password(length, use_special_chars)
    pwd_display.set(pwd)
root = tk.Tk()
root.title("Password Generator")
pwd_display = StringVar(root)
label = tk.Label(root, textvariable=pwd_display, font=('Arial', 14))
label.pack()

length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_var = IntVar(root, value=12)
length_entry = tk.Entry(root, textvariable=length_var)
length_entry.pack()
special_chars_var = IntVar(root)
special_chars_check = Checkbutton(root, text="Include Special Characters", variable=special_chars_var)
special_chars_check.pack()
generate_btn = tk.Button(root, text="Generate Password", command=display_password)
generate_btn.pack(pady=20)
root.mainloop()
