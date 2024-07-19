import tkinter as tk
from tkinter import *
import random

def generate_password():
    try:
        length = int(textbox.get())
    except ValueError:
        result_text.delete(1.0, END)
        result_text.insert(END, "Please enter a valid number for length.")
        return

    complexity = complexity_var.get()

    if complexity == "High":
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*'
    elif complexity == "Medium":
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    else:
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    password = ''.join(random.choice(chars) for _ in range(length))
    
    result_text.delete(1.0, END)
    result_text.insert(END, password)

root = tk.Tk()
root.title("PASSWORD GENERATOR")
root.geometry("400x300")
root.configure(bg='#2E4053')

frame = tk.Frame(root, bg='#f0f0f0')
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Length of Password", font=("Arial", 14, 'bold'), bg='#F7DC6F', fg='#333')
label.pack(side=LEFT, padx=5)

textbox = tk.Entry(frame, font=("Arial", 14), width=10, bg='#fff', fg='#333')
textbox.pack(side=LEFT, padx=5)

frame1 = tk.Frame(root, bg='#f0f0f0')
frame1.pack(padx=10, pady=10)

label = tk.Label(frame1, text="Complexity", font=("Arial", 14, 'bold'), bg='#F7DC6F', fg='#333')
label.pack(side=LEFT, padx=5)

complexity_var = StringVar(value="Low")

radiobutton_high = tk.Radiobutton(frame1, text="High", variable=complexity_var, value="High", font=("Arial", 14), bg='#f0f0f0', fg='#333', selectcolor='#e74c3c')
radiobutton_high.pack(side=LEFT, padx=5)

radiobutton_medium = tk.Radiobutton(frame1, text="Medium", variable=complexity_var, value="Medium", font=("Arial", 14), bg='#f0f0f0', fg='#333', selectcolor='#e74c3c')
radiobutton_medium.pack(side=LEFT, padx=5)

radiobutton_low = tk.Radiobutton(frame1, text="Low", variable=complexity_var, value="Low", font=("Arial", 14), bg='#f0f0f0', fg='#333', selectcolor='#e74c3c')
radiobutton_low.pack(side=LEFT, padx=5)

button = tk.Button(root, text="Generate", font=("Arial", 14, 'bold'), bg='#4CAF50', fg='#fff', command=generate_password)
button.pack(padx=10, pady=10)

result_text = tk.Text(root, font=("Arial", 14), width=30, height=5, bg='#fff', fg='#333')
result_text.pack(padx=10, pady=10)

root.mainloop()
