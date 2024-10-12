import tkinter as tk 


"""
calc
"""

calculator = tk.Tk()

button_pressed = False 

class Initialiser:
    calculator.geometry("600x600")
    calculator.title("Calculator")
    calculator.config(bg='White')

class OutputBar:    

    #global values
    output_bar_frame = tk.Frame(calculator)
    output_bar_frame.config(bg='White', height=10) #for the outputbar itself
    output_bar_frame.pack(side=tk.TOP, fill='x')

    number_bar_frame = tk.Frame(output_bar_frame)
    number_bar_frame.config(bg='White', height=10) #for the buttons
    number_bar_frame.pack(side=tk.RIGHT, fill='x')

    final_variable = 0 #sum of operation
    variable_one = 0 #first input 
    variable_two = 0 #second input
    operation = None #current operation


    # remember it is reversed
    # the most right side of the calculator -> will start as 0 
    output_label_nine = tk.Label(number_bar_frame, text='0', height=2, font=(20))
    output_label_nine.config(bg='White')
    output_label_nine.pack(side=tk.LEFT)
    

    def button_ones(self):
        bar_frame = OutputBar.output_label_nine
        bar_frame.destroy()

        one_label = tk.Label(OutputBar.number_bar_frame, text='1', height=2, font=(20))
        one_label.config(fg='Black', bg='White')
        one_label.pack(side=tk.LEFT, pady=2)   
             

    def button_twos(self):
        bar_frame = OutputBar.output_label_nine
        bar_frame.destroy()
        
        two_label = tk.Label(OutputBar.number_bar_frame, text='2', height=2, font=(20))
        two_label.config(fg='Black', bg='White')
        two_label.pack(side=tk.LEFT, pady=2)
        
        
    def button_threes(self):
        bar_frame = OutputBar.output_label_nine
        bar_frame.destroy()
        
        three_label = tk.Label(OutputBar.number_bar_frame, text='3', height=2, font=(20))
        three_label.config(fg='Black', bg='White')
        three_label.pack(side=tk.LEFT, pady=2)
        

    def button_fours(self):
        bar_frame = OutputBar.output_label_nine
        bar_frame.destroy()
        
        four_label = tk.Label(OutputBar.number_bar_frame, text='4', height=2, font=(20))
        four_label.config(fg='Black', bg='White')
        four_label.pack(side=tk.LEFT, pady=2)
        

    def button_fives(self):
        bar_frame = OutputBar.output_label_nine
        bar_frame.destroy()
        
        five_label = tk.Label(OutputBar.number_bar_frame, text='5', height=2, font=(20))
        five_label.config(fg='Black', bg='White')
        five_label.pack(side=tk.LEFT, pady=2)
        

    def button_sixs(self):
        bar_frame = OutputBar.output_label_nine
        bar_frame.destroy()
        
        six_label = tk.Label(OutputBar.number_bar_frame, text='6', height=2, font=(20))
        six_label.config(fg='Black', bg='White')
        six_label.pack(side=tk.LEFT, pady=2)
        

    def button_sevens(self):
        bar_frame = OutputBar.output_label_nine
        bar_frame.destroy()
        
        seven_label = tk.Label(OutputBar.number_bar_frame, text='7', height=2, font=(20))
        seven_label.config(fg='Black', bg='White')
        seven_label.pack(side=tk.LEFT, pady=2)
        

    def button_eights(self):
        bar_frame = OutputBar.output_label_nine
        bar_frame.destroy()
        
        eight_label = tk.Label(OutputBar.number_bar_frame, text='8', height=2, font=(20))
        eight_label.config(fg='Black', bg='White')
        eight_label.pack(side=tk.LEFT, pady=2)
        

    def button_nines(self):
        bar_frame = OutputBar.output_label_nine
        bar_frame.destroy()
        
        nine_label = tk.Label(OutputBar.number_bar_frame, text='9', height=2, font=(20))
        nine_label.config(fg='Black', bg='White')
        nine_label.pack(side=tk.LEFT, pady=2)
        

    def a_c_button(self):

        bar_frame = OutputBar.number_bar_frame

        for widget in bar_frame.winfo_children():
            widget.pack_forget() #clears the array 
          

        global final_variable 
        final_variable = 0
    

    def add_buttons(self):
       
       bar_frame = OutputBar.number_bar_frame
       widgets = bar_frame.winfo_children()
       initial_value = None
       global operation
       operation = '+'
       
       for widget in widgets:
           
           initial_value = widget.cget("text")

           widget.pack_forget() #clears the bar

           if initial_value != '0':
               global variable_one 
               variable_one = initial_value
               
           else:
               pass
           
    def minus_buttons(self): 
       
       bar_frame = OutputBar.number_bar_frame
       widgets = bar_frame.winfo_children()
       global operation
       operation = '-'

       for widget in widgets:
           
           initial_value = widget.cget("text")

           widget.pack_forget() #clears the bar

           if initial_value != '0':
               global variable_one 
               variable_one = initial_value
               
           else:
               pass
        
    def times_buttons(self): 
    
       bar_frame = OutputBar.number_bar_frame
       widgets = bar_frame.winfo_children()
       global operation
       operation = 'x'

       for widget in widgets:
           
           initial_value = widget.cget("text")

           widget.pack_forget() #clears the bar

           if initial_value != '0':
               global variable_one 
               variable_one = initial_value
               
           else:
               pass


    def divide_buttons(self):
       
       bar_frame = OutputBar.number_bar_frame
       widgets = bar_frame.winfo_children()
       global operation
       operation = '/'

       for widget in widgets:
           
           initial_value = widget.cget("text")

           widget.pack_forget() #clears the bar

           if initial_value != '0':
               global variable_one 
               variable_one = initial_value
               
           else:
               pass


    def equal_buttons(self):
        bar_frame = OutputBar.number_bar_frame
        for widget in bar_frame.winfo_children():
            global variable_two 
            variable_two = widget.cget("text")
            widget.pack_forget()


        global operation
        global final_variable
        global variable_one

        if operation == '+':
             
            final_variable = str(float(variable_one) + float(variable_two))

        elif operation == 'x':
             
            final_variable = str(float(variable_one) * float(variable_two))

        elif operation == '/':
             
            final_variable = str(float(variable_one) / float(variable_two))
        
        elif operation == '-':
            
            final_variable = str(float(variable_one) - float(variable_two))
        
        answer_label = tk.Label(OutputBar.number_bar_frame, text=f"{final_variable}", height=2, font=(20))
        answer_label.config(bg='White', fg='Black', font=(20))
        answer_label.pack(side=tk.RIGHT)        
        

            
     


class Button(OutputBar):

    #change later

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
    button_width = 6

    button_frame = tk.Frame(calculator)
    button_frame.config(bg='White')
    button_frame.pack(side=tk.TOP, anchor=tk.W, pady=5, fill='x', expand=False)

    #row 1 

    row_one_frame = tk.Frame(button_frame)
    row_one_frame.config(bg='White')
    row_one_frame.pack(side=tk.TOP, pady=5, fill='x', expand=True)

    ac_button = tk.Button(row_one_frame, text='AC', font=button_size, width=button_width, command=ac_button)
    ac_button.grid(row=0, column=0, padx=10)

    plus_minus_button = tk.Button(row_one_frame, text='+/-', font=button_size, width=button_width)
    plus_minus_button.grid(row=0, column=1, padx=10)

    percentage_button = tk.Button(row_one_frame, text='%', font=button_size, width=button_width)
    percentage_button.grid(row=0, column=2, padx=10)

    divide_button = tk.Button(row_one_frame, text='÷', bg='White', font=button_size, width=button_width, command=divide_buttonn)
    divide_button.grid(row=0, column=3, padx=10)

    #row 2

    row_two_frame = tk.Frame(button_frame)
    row_two_frame.config(bg='White')
    row_two_frame.pack(side=tk.TOP, fill='x', expand=False)

    seven_button = tk.Button(row_two_frame, text='7', font=button_size, width=button_width, command=button_seven)
    seven_button.grid(row=1, column=0, padx=10, pady=2)

    eight_button = tk.Button(row_two_frame, text='8', font=button_size, width=button_width, command=button_eight)
    eight_button.grid(row=1, column=1, padx=10)

    nine_button = tk.Button(row_two_frame, text='9', font=button_size, width=button_width, command=button_nine)
    nine_button.grid(row=1, column=2, padx=10)

    times_button = tk.Button(row_two_frame, text='x', bg='White', font=button_size, width=button_width, command=times_button)
    times_button.grid(row=1, column=3, padx=10)

    #row 3 

    row_three_frame = tk.Frame(button_frame)
    row_three_frame.config(bg='White')
    row_three_frame.pack(side=tk.TOP, fill='x', expand=False)

    four_button = tk.Button(row_three_frame, text='4', font=button_size, width=button_width, command=button_four)
    four_button.grid(row=2, column=0, padx=10, pady=2)

    five_button = tk.Button(row_three_frame, text='5', font=button_size, width=button_width, command=button_five)
    five_button.grid(row=2, column=1, padx=10)

    six_button = tk.Button(row_three_frame, text='6', font=button_size, width=button_width, command=button_six)
    six_button.grid(row=2, column=2, padx=10)

    minus_button = tk.Button(row_three_frame, text='-', bg='White', font=button_size, width=button_width, command=minus_buttonn)
    minus_button.grid(row=2, column=3, padx=10)

    #row 4
    row_four_frame =tk.Frame(button_frame)
    row_four_frame.config(bg='White')
    row_four_frame.pack(side=tk.TOP, fill='x', expand=False, pady=5)

    one_button = tk.Button(row_three_frame, text='1', font=button_size, width=button_width, command=button_one)
    one_button.grid(row=3, column=0, padx=10, pady=2)

    two_button = tk.Button(row_three_frame, text='2', font=button_size, width=button_width, command=button_two)
    two_button.grid(row=3, column=1, padx=10)

    three_button = tk.Button(row_three_frame, text='3', font=button_size, width=button_width, command=button_three)
    three_button.grid(row=3, column=2, padx=10)

    plus_button = tk.Button(row_three_frame, text='+', bg='White', font=button_size, width=button_width, command=add_button)
    plus_button.grid(row=3, column=3, padx=10)
    
    #row 5 

    row_five_frame = tk.Frame(button_frame)
    row_five_frame.config(bg='White')
    row_five_frame.pack(side=tk.TOP, fill='x', expand=False, pady=5)

    zero_button = tk.Button(row_four_frame, text='0', font=button_size, width=button_width)
    zero_button.grid(row=4, column=0, padx=10, pady=2, columnspan=4)

    decimal_button = tk.Button(row_four_frame, text='.', font=button_size, width=button_width)
    decimal_button.grid(row=4, column=5, padx=10)

    equal_buttons = tk.Button(row_four_frame, text='=', bg='White', font=button_size, width=button_width, command=equal_button)
    equal_buttons.grid(row=4, column=6, padx=10)



Initialiser()
OutputBar()
Button()

calculator.mainloop()
