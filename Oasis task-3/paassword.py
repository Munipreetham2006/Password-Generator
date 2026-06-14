import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4!")
            return

        chars = ""

        if upper_var.get():
            chars += string.ascii_uppercase
        if lower_var.get():
            chars += string.ascii_lowercase
        if digit_var.get():
            chars += string.digits
        if symbol_var.get():
            chars += string.punctuation

        if not chars:
            messagebox.showerror("Error", "Select at least one character type!")
            return

        password = ''.join(secrets.choice(chars) for _ in range(length))

        password_var.set(password)
        check_strength(password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")

def check_strength(password):
    score = 0

    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    if len(password) >= 12:
        score += 1

    if score <= 2:
        strength_label.config(text="Strength: Weak")
    elif score <= 4:
        strength_label.config(text="Strength: Medium")
    else:
        strength_label.config(text="Strength: Strong")

def copy_password():
    password = password_var.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")


def toggle_password():
    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

def save_password():
    password = password_var.get()

    if password:
        with open("passwords.txt", "a") as file:
            file.write(password + "\n")

        messagebox.showinfo("Saved", "Password saved to passwords.txt")

root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("450x450")
root.resizable(False, False)

tk.Label(
    root,
    text="Advanced Password Generator",
    font=("Arial", 16, "bold")
).pack(pady=10)

tk.Label(root, text="Password Length").pack()

length_entry = tk.Entry(root)
length_entry.pack()
length_entry.insert(0, "12")

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Uppercase", variable=upper_var).pack(anchor="w", padx=120)
tk.Checkbutton(root, text="Lowercase", variable=lower_var).pack(anchor="w", padx=120)
tk.Checkbutton(root, text="Numbers", variable=digit_var).pack(anchor="w", padx=120)
tk.Checkbutton(root, text="Symbols", variable=symbol_var).pack(anchor="w", padx=120)

tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    width=20
).pack(pady=10)

password_var = tk.StringVar()

password_entry = tk.Entry(
    root,
    textvariable=password_var,
    width=30,
    justify="center",
    show="*"
)
password_entry.pack()

show_var = tk.BooleanVar()

tk.Checkbutton(
    root,
    text="Show Password",
    variable=show_var,
    command=toggle_password
).pack()

strength_label = tk.Label(root, text="Strength: ")
strength_label.pack(pady=5)

tk.Button(root, text="Copy Password", command=copy_password, width=20).pack(pady=5)

tk.Button(root, text="Save Password", command=save_password, width=20).pack(pady=5)

root.mainloop()