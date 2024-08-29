import tkinter as tk 


"""
calc
"""

lee = tk.Tk()

class Initialiser:
    lee.geometry("400x400")
    lee.title("Calculator")

class OutputBar:    
    title_frame = tk.Frame(lee)
    title_frame.pack(side=tk.TOP, pady=5)

    output_bar = tk.Text(title_frame, height=3, width=50)
    output_bar.pack(side=tk.TOP)


class Button:
    button_frame = tk.Frame(lee)
    button_frame.pack(side=tk.LEFT)

    ac_button = tk.Button(button_frame, text='AC')
    ac_button.grid(row=0, column=0)

    plus_minus_button = tk.Button(button_frame, text='+/-')
    plus_minus_button.grid(row=0, column=1)

    percentage_button = tk.Button(button_frame, text='%')
    percentage_button.grid(row=0, column=2)

    divide_button = tk.Button(button_frame, text='÷', bg='Orange')
    divide_button.grid(row=0, column=3)


Initialiser()
OutputBar()
Button()

lee.mainloop()