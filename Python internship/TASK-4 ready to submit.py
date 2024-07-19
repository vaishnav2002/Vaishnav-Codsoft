import tkinter as tk
from tkinter import *
import random

root = tk.Tk()
root.geometry("800x800")
root.title("ROCK PAPER SCISSORS GAME")
root.configure(bg="#282C34")

label = tk.Label(root, text="ROCK PAPER SCISSORS GAME", font=("Arial", 20), fg="#61AFEF", bg="#282C34")
label.pack(padx=10, pady=10)

frame = tk.Frame(root, bg="#282C34")
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="USER CHOICE:", font=("Arial", 15), fg="#61AFEF", bg="#282C34")
label.pack(side="left", padx=10)

textbox = Text(frame, height=3, font=("Arial", 15), bg="#ABB2BF", fg="#282C34")
textbox.pack(padx=10, pady=10)

def play_game():
    while True:
        user_choice = textbox.get("1.0", END).strip().lower()
        if user_choice in ["rock", "paper", "scissors"]:
            break
        else:
            result_textbox.delete("1.0", END)
            result_textbox.insert(END, "Invalid option. Please enter rock, paper, or scissors.")
            return
    
    textbox.delete("1.0", END)  # Clear user input area
    
    # Generate computer's choice
    computer_choice_num = random.randint(1, 3)
    if computer_choice_num == 1:
        computer_choice = "rock"
    elif computer_choice_num == 2:
        computer_choice = "paper"
    elif computer_choice_num == 3:
        computer_choice = "scissors"
    else:
        result_textbox.delete("1.0", END)
        result_textbox.insert(END, "Something went wrong with computer's choice.")
        return
    
    # Display user and computer choices in the GUI
    result_textbox.delete("1.0", END)
    result_textbox.insert(END, f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n\n")
    
    # Determine game result
    if user_choice == computer_choice:
        result_textbox.insert(END, "It's a TIE")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result_textbox.insert(END, "YOU WIN")
    else:
        result_textbox.insert(END, "FAILED")

button = tk.Button(root, text="PLAY", font=("Arial", 15), fg="#FFFFFF", bg="#98C379", bd=5, command=play_game)
button.pack(padx=10, pady=10)

frame1 = tk.Frame(root, bg="#282C34")
frame1.pack(padx=20, pady=20)

label = tk.Label(frame1, text="GAME RESULT:", font=("Arial", 15), fg="#61AFEF", bg="#282C34")
label.pack(side="left", padx=10)

result_textbox = Text(frame1, height=5, font=("Arial", 15), bg="#ABB2BF", fg="#282C34")
result_textbox.pack(padx=10, pady=10)

root.mainloop()
