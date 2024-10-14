import tkinter as tk 
import random as random
import time as time 

gui = tk.Tk()

class Initialiser:

    gui.geometry("400x400")
    gui.title("Rock Paper Scissors")
    gui.config(bg='Black')

class Commands:

    #parameters
    'paper' > 'rock'
    'rock' > 'scissors'
    'scissors' > 'paper'

    choice_list = ['rock', 'paper', 'scissors']

    system_value = random.choice(choice_list)

    
    def rock(self):

        user_input = 'rock'

        if user_input > system_value:

            win_label = tk.Label(gui, text='You win!', font=(20), fg='Black', bg='White')
            win_label.pack(side=tk.TOP)

        elif user_input < system_value:

            lose_label = tk.Label(gui, text='You lose!', font=(20), fg='Black', bg='White')
            lose_label.pack(side=tk.TOP)

        elif user_input == system_value: 

            tie_label = tk.Label(gui, text='You tied', font=(20), fg='Black', bg='White')
            tie_label.pack(side=tk.TOP)

            


        

            


class Buttons(Commands):

    rock_command = Commands.rock

    button_frame = tk.Frame(gui)
    button_frame.pack(side=tk.BOTTOM, pady=5)

    rock_button = tk.Button(button_frame, text='Rock', font=(20), fg='Black', command=rock_command)
    rock_button.grid(row=0, column=0, pady=5)

    paper_button = tk.Button(button_frame, text='Paper', font=(20), fg='Black')
    paper_button.grid(row=0, column=1, pady=5)

    scissor_button = tk.Button(button_frame, text='Scissor', font=(20), fg='Black')
    scissor_button.grid(row=0, column=2, pady=5)



Initialiser()
Buttons()

gui.mainloop()


