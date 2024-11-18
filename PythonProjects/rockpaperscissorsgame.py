import random as random
import tkinter as tk 



class Initialiser:

    value_list = []

    def rock(self):
        value_classification = 'rock'
        value_list.append[value_classification]

        for word in value_list:
            if word = 'paper':
                



    def window_frame(self):
        window = tk.Tk()

        window.geometry("400x400")


        #first box 
        rock_box = tk.Button(window, text='Rock', font=(20))
        rock_box.pack()

        #second box 
        paper_box = tk.Button(window, text='Paper', font=(20))
        paper_box.pack()

        #third box
        scissors_box = tk.Button(window, text='Scissors', font=(20))
        scissors_box.pack()

        window.mainloop()
        



frame_initialiser = Initialiser()
frame_initialiser.window_frame()


