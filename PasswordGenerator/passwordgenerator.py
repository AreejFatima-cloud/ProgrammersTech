import random
import string
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

# Function For Password Generate Button
def generate_password():
    try:
        length = int(my_entry.get())
        if length <= 0:
            raise ValueError
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))
        pw_entry.config(state='normal')
        pw_entry.delete(0, END)
        pw_entry.insert(0, password)
        pw_entry.config(state='readonly')
        messagebox.showinfo("Password Generated", "Password generated successfully!")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of characters.")

# Function For Copy Button
def Copy_Password():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())
    messagebox.showinfo("Password Copied", "Password copied to clipboard!")

# creating themed tkinter window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.config(bg='white')

# Title
title_label = ttk.Label(root, text="Random Strong Password Generator", font=("Helvetica", 16, "bold"), anchor=tk.CENTER, background='white')
title_label.pack(pady=(20, 10))

# Frame for length input
length_frame = LabelFrame(root, text="How Many Characters?", bg='white')
length_frame.pack(pady=10)

my_entry = Entry(length_frame, font=("Helvetica", 14))
my_entry.pack(padx=20, pady=20)

# Output field
pw_entry = Entry(root, font=("Helvetica", 14), state='readonly')
pw_entry.pack(pady=20)

# Frame for buttons
button_frame = Frame(root, bg='white')
button_frame.pack(pady=20)

# Generate Button
generate_button = Button(button_frame, text="Generate Password", command=generate_password, font=("Helvetica", 12), bg='white')
generate_button.grid(row=0, column=0, padx=10)

# Copy Button
copy_button = Button(button_frame, text="Copy", command=Copy_Password, font=("Helvetica", 12), bg='white')
copy_button.grid(row=0, column=1, padx=10)

# main loop
root.mainloop()
