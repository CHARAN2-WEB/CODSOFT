import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def on_button_click(choice):
    user_choice = choice
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    
    result_text = f"You chose {user_choice}, computer chose {computer_choice}.\n"
    
    if winner == 'tie':
        result_text += "It's a tie!"
    elif winner == 'user':
        result_text += "You win!"
    else:
        result_text += "You lose!"
    
    messagebox.showinfo("Result", result_text)

root = tk.Tk()
root.title("Rock Paper Scissors Game")

tk.Label(root, text="Choose rock, paper, or scissors:").pack()
button_font = ('Arial', 14, 'bold')
button_bg = '#0D47A1'
button_fg = 'white'
button_active_bg = '#1565C0'

tk.Button(root, text="Rock", font=button_font, bg=button_bg, fg=button_fg,
          activebackground=button_active_bg, command=lambda: on_button_click('rock')).pack(side=tk.LEFT)
tk.Button(root, text="Paper", font=button_font, bg=button_bg, fg=button_fg,
          activebackground=button_active_bg, command=lambda: on_button_click('paper')).pack(side=tk.LEFT)
tk.Button(root, text="Scissors", font=button_font, bg=button_bg, fg=button_fg,
          activebackground=button_active_bg, command=lambda: on_button_click('scissors')).pack(side=tk.LEFT)
root.mainloop()
