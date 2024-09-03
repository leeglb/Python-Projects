#3 sections of the app
#Random number generator for +, - 
#Word speller 

import tkinter as tk 
import random as random 



lee = tk.Tk()
lee.geometry("400x400")

class Title:

    title_frame = tk.Frame(lee) 
    title_frame.config(bg='White', height=50)
    title_frame.pack(side=tk.TOP, fill='x')

    title_text = tk.Label(title_frame, text='Tutoring App', fg='Black', bg='White', font=(20))
    title_text.pack(side=tk.TOP)

class ButtonFunction:

    def addition_subtraction_page(self):
        pass

class MainFrame:

    app_frame = tk.Frame(lee)
    app_frame.pack(side=tk.TOP, pady=5)

    first_button = tk.Button(app_frame, text='Addition and Subtraction Of Large Numbers', bg='White')
    first_button.pack(side=tk.TOP)

    second_button = tk.Button(app_frame, text='Spelling Checker', bg='White')
    second_button.pack(side=tk.TOP, pady=5)

    third_button = tk.Button(app_frame, text='Sentence Writer', bg='White')
    third_button.pack(side=tk.TOP)

A = Title()
B = MainFrame()

lee.mainloop()