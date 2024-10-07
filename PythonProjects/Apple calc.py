import tkinter as tk 


"""
calc
"""

lee = tk.Tk()

button_pressed = False 

class Initialiser:
    lee.geometry("400x300")
    lee.title("Calculator")
    lee.config(bg='Black')

class OutputBar:    

    #global values
    output_bar_frame = tk.Frame(lee)
    output_bar_frame.config(bg="Black", height=10)
    output_bar_frame.pack(side=tk.TOP, fill='x')

    number_bar_frame = tk.Frame(output_bar_frame)
    number_bar_frame.config(bg='Black', height=10)
    number_bar_frame.pack(side=tk.RIGHT, fill='x')

    final_variable = 0 
    


    # remember it is reversed
    

    output_label_nine = tk.Label(number_bar_frame, text='0', height=2, font=(20))
    output_label_nine.config(bg='Black')
    output_label_nine.pack(side=tk.LEFT)
    

    def button_ones(self):
        a = OutputBar.output_label_nine
        a.destroy()


        one_label = tk.Label(OutputBar.number_bar_frame, text='1', height=2, font=(20))
        one_label.config(fg='White', bg='Black')
        one_label.pack(side=tk.LEFT, pady=2)   
             

    def button_twos(self):
        a = OutputBar.output_label_nine
        a.destroy()
        
        two_label = tk.Label(OutputBar.number_bar_frame, text='2', height=2, font=(20))
        two_label.config(fg='White', bg='Black')
        two_label.pack(side=tk.LEFT, pady=2)
        
        
    def button_threes(self):
        a = OutputBar.output_label_nine
        a.destroy()
        
        three_label = tk.Label(OutputBar.number_bar_frame, text='3', height=2, font=(20))
        three_label.config(fg='White', bg='Black')
        three_label.pack(side=tk.LEFT, pady=2)
        

    def button_fours(self):
        a = OutputBar.output_label_nine
        a.destroy()
        
        four_label = tk.Label(OutputBar.number_bar_frame, text='4', height=2, font=(20))
        four_label.config(fg='White', bg='Black')
        four_label.pack(side=tk.LEFT, pady=2)
        

    def button_fives(self):
        a = OutputBar.output_label_nine
        a.destroy()
        
        five_label = tk.Label(OutputBar.number_bar_frame, text='5', height=2, font=(20))
        five_label.config(fg='White', bg='Black')
        five_label.pack(side=tk.LEFT, pady=2)
        

    def button_sixs(self):
        a = OutputBar.output_label_nine
        a.destroy()
        
        six_label = tk.Label(OutputBar.number_bar_frame, text='6', height=2, font=(20))
        six_label.config(fg='White', bg='Black')
        six_label.pack(side=tk.LEFT, pady=2)
        

    def button_sevens(self):
        a = OutputBar.output_label_nine
        a.destroy()
        
        seven_label = tk.Label(OutputBar.number_bar_frame, text='7', height=2, font=(20))
        seven_label.config(fg='White', bg='Black')
        seven_label.pack(side=tk.LEFT, pady=2)
        

    def button_eights(self):
        a = OutputBar.output_label_nine
        a.destroy()
        
        eight_label = tk.Label(OutputBar.number_bar_frame, text='8', height=2, font=(20))
        eight_label.config(fg='White', bg='Black')
        eight_label.pack(side=tk.LEFT, pady=2)
        

    def button_nines(self):
        a = OutputBar.output_label_nine
        a.destroy()
        
        nine_label = tk.Label(OutputBar.number_bar_frame, text='9', height=2, font=(20))
        nine_label.config(fg='White', bg='Black')
        nine_label.pack(side=tk.LEFT, pady=2)
        

    def a_c_button(self): 
        a = OutputBar.number_bar_frame
        for widget in a.winfo_children():
            widget.pack_forget() #clears the array 

        global final_variable 
        final_variable = 0
    

    def add_buttons(self):
       a = OutputBar.number_bar_frame
       for widgets in a.winfo_children():
           b = widgets.cget("text")
           widgets.pack_forget()

           global final_variable
           number_variable = b
           final_variable = str(int(number_variable) + int(number_variable))
           
    
    def equal_buttons(self):
        a = OutputBar.number_bar_frame
        for widget in a.winfo_children():
            widget.destroy()

        global final_variable
        
        answer_label = tk.Label(OutputBar.number_bar_frame, text=f"{final_variable}", height=2, font=(20))
        answer_label.config(bg='Black')
        answer_label.pack(side=tk.RIGHT)
        
    def times_buttons(self): 
        
       a = OutputBar.number_bar_frame
       for widgets in a.winfo_children():
           b = widgets.cget("text")
           widgets.pack_forget()

           global final_variable
           number_variable = b
           final_variable = str(int(number_variable) * int(number_variable))

    def minus_buttons(self): 
        
       a = OutputBar.number_bar_frame
       for widgets in a.winfo_children():
           b = widgets.cget("text")
           widgets.pack_forget()

           global final_variable
           number_variable = b
           final_variable = str(int(number_variable) - int(number_variable))

    def divide_buttons(self):
        
        a = OutputBar.number_bar_frame
        for widgets in a.winfo_children():
           b = widgets.cget("text")
           widgets.pack_forget()

           global final_variable
           number_variable = b
           final_variable = str(int(number_variable) / int(number_variable))

            
        

            
     


class Button(OutputBar):

    A = OutputBar()
    button_one = A.button_ones
    button_two = A.button_twos
    button_three = A.button_threes
    button_four = A.button_fours
    button_five = A.button_fives
    button_six = A.button_sixs
    button_seven = A.button_sevens
    button_eight = A.button_eights
    button_nine = A.button_nines
    ac_button = A.a_c_button
    add_button = A.add_buttons
    equal_button = A.equal_buttons
    times_button = A.times_buttons
    minus_buttonn = A.minus_buttons
    divide_buttonn = A.divide_buttons



    button_size = 30
    button_width = 3

    button_frame = tk.Frame(lee)
    button_frame.config(bg='Black')
    button_frame.pack(side=tk.TOP, anchor=tk.W, pady=5, fill='x', expand=False)

    #row 1 

    row_one_frame = tk.Frame(button_frame)
    row_one_frame.config(bg='Black')
    row_one_frame.pack(side=tk.TOP, pady=5, fill='x', expand=False)

    ac_button = tk.Button(row_one_frame, text='AC', font=button_size, width=button_width, command=ac_button)
    ac_button.grid(row=0, column=0, padx=10)

    plus_minus_button = tk.Button(row_one_frame, text='+/-', font=button_size, width=button_width)
    plus_minus_button.grid(row=0, column=1, padx=10)

    percentage_button = tk.Button(row_one_frame, text='%', font=button_size, width=button_width)
    percentage_button.grid(row=0, column=2, padx=10)

    divide_button = tk.Button(row_one_frame, text='÷', bg='Orange', font=button_size, width=button_width, command=divide_buttonn)
    divide_button.grid(row=0, column=3, padx=10)

    #row 2

    row_two_frame = tk.Frame(button_frame)
    row_two_frame.config(bg='Black')
    row_two_frame.pack(side=tk.TOP, fill='x', expand=False)

    seven_button = tk.Button(row_two_frame, text='7', font=button_size, width=3, command=button_seven)
    seven_button.grid(row=1, column=0, padx=10, pady=2)

    eight_button = tk.Button(row_two_frame, text='8', font=button_size, width=button_width, command=button_eight)
    eight_button.grid(row=1, column=1, padx=10)

    nine_button = tk.Button(row_two_frame, text='9', font=button_size, width=button_width, command=button_nine)
    nine_button.grid(row=1, column=2, padx=10)

    times_button = tk.Button(row_two_frame, text='x', bg='Orange', font=button_size, width=button_width, command=times_button)
    times_button.grid(row=1, column=3, padx=10)

    #row 3 

    row_three_frame = tk.Frame(button_frame)
    row_three_frame.config(bg='Black')
    row_three_frame.pack(side=tk.TOP, fill='x', expand=False)

    four_button = tk.Button(row_three_frame, text='4', font=button_size, width=3, command=button_four)
    four_button.grid(row=2, column=0, padx=10, pady=2)

    five_button = tk.Button(row_three_frame, text='5', font=button_size, width=button_width, command=button_five)
    five_button.grid(row=2, column=1, padx=10)

    six_button = tk.Button(row_three_frame, text='6', font=button_size, width=button_width, command=button_six)
    six_button.grid(row=2, column=2, padx=10)

    minus_button = tk.Button(row_three_frame, text='-', bg='Orange', font=button_size, width=button_width, command=minus_buttonn)
    minus_button.grid(row=2, column=3, padx=10)

    #row 4
    row_four_frame =tk.Frame(button_frame)
    row_four_frame.config(bg='Black')
    row_four_frame.pack(side=tk.TOP, fill='x', expand=False, pady=5)

    one_button = tk.Button(row_three_frame, text='1', font=button_size, width=3, command=button_one)
    one_button.grid(row=3, column=0, padx=10, pady=2)

    two_button = tk.Button(row_three_frame, text='2', font=button_size, width=button_width, command=button_two)
    two_button.grid(row=3, column=1, padx=10)

    three_button = tk.Button(row_three_frame, text='3', font=button_size, width=button_width, command=button_three)
    three_button.grid(row=3, column=2, padx=10)

    plus_button = tk.Button(row_three_frame, text='+', bg='Orange', font=button_size, width=button_width, command=add_button)
    plus_button.grid(row=3, column=3, padx=10)
    
    #row 5 

    row_five_frame = tk.Frame(button_frame)
    row_five_frame.config(bg='Black')
    row_five_frame.pack(side=tk.TOP, fill='x', expand=False, pady=5)

    zero_button = tk.Button(row_four_frame, text='0', font=button_size, width=9)
    zero_button.grid(row=4, column=0, padx=10, pady=2)

    decimal_button = tk.Button(row_four_frame, text='.', font=button_size, width=button_width)
    decimal_button.grid(row=4, column=1, padx=10)

    equal_buttons = tk.Button(row_four_frame, text='=', bg='Orange', font=button_size, width=button_width, command=equal_button)
    equal_buttons.grid(row=4, column=2, padx=10)



Initialiser()
OutputBar()
Button()

lee.mainloop()
