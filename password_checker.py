import tkinter as tk
from tkinter import ttk
import re
import random
import string

def check_password(password):
	if len(password) < 8:
		return "Password must be more than 8 characters!"
	if not re.search(r"[0-9]", password):
		return "Password must contain digit!"
	if not re.search(r"[A-Z]", password):
		return "Password must contain Uppercase!"
	if not re.search(r"[a-z]", password):
		return "Password must contain Lowercase!"
	if not re.search(r"[!@#$%^&*()_=+*/<>?{}\[\]:;-]", password):
		return "Password must contain Special character!"
	return "Strong"

def get_strength_value(password):
	strength=0
	if len(password) >= 8:
		strength += 1
	if re.search(r"[A-Z]", password):
		strength += 1
	if re.search(r"[a-z]", password):
		strength += 1
	if re.search(r"[0-9]", password):
		strength += 1
	if re.search(r"[!@#$%^&*()_=+*/<>?{}\[\]:;-]", password):
		strength += 1
	return strength*20


def generate_password(length=12):
	if length < 8:
		return "Length must be at least 8"

	lowercase=string.ascii_lowercase
	uppercase=string.ascii_uppercase
	digit=string.digits
	special=r"!@#$%^&*()_=+*/<>?{}\[\]:;-"

	password=[
		random.choice(lowercase),
		random.choice(uppercase),
		random.choice(digit),
		random.choice(special)
	]

	all_char=lowercase+uppercase+digit+special
	password+=random.choices(all_char,k=length-4)
	random.shuffle(password)
	return ''.join(password)

def on_check():
	pwd = entry.get()
	result = check_password(pwd)
	strength = get_strength_value(pwd)
	progress['value']=strength
	if result == "Strong":
		feedback.config(text="Strong Password",fg="green")
	else:
		feedback.config(text=f"{result}",fg="red")

def on_generate():
	pwd=generate_password()
	entry.delete(0, tk.END)
	entry.insert(0, pwd)
	on_check()

def toggle_password():
	if show_var.get():
		entry.config(show='')
	else:
		entry.config(show="*")

root = tk.Tk()
root.title("Password Tool")
show_var = tk.BooleanVar()

tk.Label(root, text="Enter Password:").pack(pady=5)
entry = tk.Entry(root, width=30, show='*')
entry.pack(pady=5)

tk.Checkbutton(root, text="Show Password", variable=show_var, command=toggle_password).pack(pady=5)

tk.Button(root, text="Check Strength", command=on_check).pack(pady=5)

progress = ttk.Progressbar(root, length=200, maximum=100)
progress.pack(pady=5)

feedback = tk.Label(root, text="")
feedback.pack(pady=5)

tk.Button(root, text="Generate Strong Password", command=on_generate).pack(pady=10)

root.mainloop()


