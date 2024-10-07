#3 sections of the app
#Random number generator for +, - 
#Word speller 

import tkinter as tk 
import random as random 



lee = tk.Tk()
lee.config(bg='Black')
lee.geometry("400x400")

class Title:

    title_frame = tk.Frame(lee) 
    title_frame.config(bg='White', height=50)
    title_frame.pack(side=tk.TOP, fill='x')

    title_text = tk.Label(title_frame, text='Tutoring App', fg='Black', bg='White', font=(20))
    title_text.pack(side=tk.TOP)

class ButtonFunction(Title):

    def addition_subtraction_page():

        app_frame = MainFrame.app_frame
        app_frame.pack_forget() 

        addition_subtraction_frame = tk.Frame(Title.title_frame)
        addition_subtraction_frame.pack(side=tk.TOP)
        
        number_list_one = range(100,500)
        random_value_one = random.choice(number_list_one)

        number_list_two = range(501,9999)
        random_value_two = random.choice(number_list_two)

        final_value = random_value_two - random_value_one

        input_label_title = tk.Label(lee, text='Enter Your Answer', font=(20))
        input_label_title.pack(side=tk.TOP, pady=5)
 
        input_label_text = tk.Text(lee, height=2, width=10)
        input_label_text.pack(side=tk.TOP)


class MainFrame(ButtonFunction):

    app_frame = tk.Frame(lee)
    app_frame.config(bg='Black')
    app_frame.pack(side=tk.TOP, pady=5)

    first_button = tk.Button(app_frame, text='Addition and Subtraction Of Large Numbers', bg='White', command=ButtonFunction.addition_subtraction_page)
    first_button.pack(side=tk.TOP)

    second_button = tk.Button(app_frame, text='Spelling Checker', bg='White')
    second_button.pack(side=tk.TOP, pady=5)

    third_button = tk.Button(app_frame, text='Sentence Writer', bg='White')
    third_button.pack(side=tk.TOP)

A = Title()
B = MainFrame()

lee.mainloop()
