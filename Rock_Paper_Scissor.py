import tkinter as tk
import random


root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.config(bg="blue")
root.geometry("630x500")
root.resizable(False,False)



user_score = 0
computer_score = 0



def play(user_choice):
    global user_score, computer_score
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
            (user_choice == 'Paper' and computer_choice == 'Rock') or \
            (user_choice == 'Scissors' and computer_choice == 'Paper'):
        user_score += 1
        result_label.config(text="You win! Computer chose " + computer_choice)
    else:
        computer_score += 1
        result_label.config(text="Computer wins! Computer chose " + computer_choice)

    # Update the score labels
    user_score_label.config(text="User Score: " + str(user_score))
    computer_score_label.config(text="Computer Score: " + str(computer_score))



def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Let's play!")
    user_score_label.config(text="User Score: 0")
    computer_score_label.config(text="Computer Score: 0")



rock_button = tk.Button(root, text="Rock", font=10, width=20, height=5, command=lambda: play('Rock'))
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button = tk.Button(root, text="Paper",  font=10,width=20,height=5, command=lambda: play('Paper'))
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissors_button = tk.Button(root, text="Scissors", font=10, width=20,height=5, command=lambda: play('Scissors'))
scissors_button.grid(row=0, column=2, padx=10, pady=10)


result_label = tk.Label(root, text="Let's play!",bg="blue",fg="white", font=("Helvetica", 14,"bold"))
result_label.grid(row=1, column=0, columnspan=3)

reset_button = tk.Button(root, text="Reset", width=10, command=reset_game)
reset_button.grid(row=4, column=2, padx=10, pady=10, sticky='e')


user_score_label = tk.Label(root, text="User Score: 0",bg="blue",fg="white", font=("Helvetica", 12, "bold"))
user_score_label.grid(row=3, column=0)

computer_score_label = tk.Label(root, text="Computer Score: 0",bg="blue",fg="white",font=("Helvetica", 12,"bold"))
computer_score_label.grid(row=3, column=2)


root.mainloop()
