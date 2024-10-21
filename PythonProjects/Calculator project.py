import tkinter as tk 


"""
calc
"""

calculator = tk.Tk()

button_pressed = False 

class Initialiser:
    calculator.geometry("600x270")
    calculator.title("Calculator")
    calculator.config(bg='Black')

class OutputBar:    

    #global values
    output_bar_frame = tk.Frame(calculator)
    output_bar_frame.config(bg='White', height=10) #for the outputbar frame itself
    output_bar_frame.pack(side=tk.TOP, fill='x')

    number_textbox = tk.Text(calculator)
    number_textbox.config(bg='Black', height=5)
    number_textbox.pack(side=tk.TOP, fill='x')

    number_textbox_font = (20)
    number_textbox.config(font=number_textbox_font)

    number_bar_frame = tk.Frame(output_bar_frame)
    number_bar_frame.config(bg='White', height=10) #for the buttons
    number_bar_frame.pack(side=tk.RIGHT, fill='x')

    final_variable = 0 #sum of operation
    variable_one = 0 #first input 
    variable_two = 0 #second input
    operation = None #current operation


    # remember it is reversed
    # the most right side of the calculator -> will start as 0 

    

    def button_ones(self):
        
        number_input_array = OutputBar.number_textbox
        number_input_value = number_input_array.get('1.0', tk.END)

        if number_input_value == "0":

            number_input_array = OutputBar.number_textbox
            number_input_array.delete('1.0', tk.END)
        else:
            text_value = "1"
            OutputBar.number_textbox.insert(tk.END, text_value) 

    def button_twos(self):

        number_input_array = OutputBar.number_textbox
        number_input_value = number_input_array.get('1.0', tk.END)

        if number_input_value == "0":

            number_input_array = OutputBar.number_textbox
            number_input_array.delete('1.0', tk.END)

        text_value = "2"

        OutputBar.number_textbox.insert(tk.END, text_value) 
        
        
    def button_threes(self):

        number_input_array = OutputBar.number_textbox
        number_input_value = number_input_array.get('1.0', tk.END)

        if number_input_value == "0":

            number_input_array = OutputBar.number_textbox
            number_input_array.delete('1.0', tk.END)
        
        text_value = "3"

        OutputBar.number_textbox.insert(tk.END, text_value) 
        

    def button_fours(self):

        number_input_array = OutputBar.number_textbox
        number_input_value = number_input_array.get('1.0', tk.END)

        if number_input_value == "0":

            number_input_array = OutputBar.number_textbox
            number_input_array.delete('1.0', tk.END)
        
        text_value = "4"

        OutputBar.number_textbox.insert(tk.END, text_value) 
        

    def button_fives(self):

        number_input_array = OutputBar.number_textbox
        number_input_value = number_input_array.get('1.0', tk.END)

        if number_input_value == "0":

            number_input_array = OutputBar.number_textbox
            number_input_array.delete('1.0', tk.END)
        
        text_value = "5"

        OutputBar.number_textbox.insert(tk.END, text_value) 
        

    def button_sixs(self):

        number_input_array = OutputBar.number_textbox
        number_input_value = number_input_array.get('1.0', tk.END)

        if number_input_value == "0":

            number_input_array = OutputBar.number_textbox
            number_input_array.delete('1.0', tk.END)
        
        text_value = "6"

        OutputBar.number_textbox.insert(tk.END, text_value) 
        

    def button_sevens(self):

        number_input_array = OutputBar.number_textbox
        number_input_value = number_input_array.get('1.0', tk.END)

        if number_input_value == "0":

            number_input_array = OutputBar.number_textbox
            number_input_array.delete('1.0', tk.END)
        
        text_value = "7"

        OutputBar.number_textbox.insert(tk.END, text_value) 
        

    def button_eights(self):

        number_input_array = OutputBar.number_textbox
        number_input_value = number_input_array.get('1.0', tk.END)

        if number_input_value == "0":

            number_input_array = OutputBar.number_textbox
            number_input_array.delete('1.0', tk.END)

        text_value = "8"

        OutputBar.number_textbox.insert(tk.END, text_value) 
        

    def button_nines(self):

        number_input_array = OutputBar.number_textbox
        number_input_value = number_input_array.get('1.0', tk.END)

        if number_input_value == "0":

            number_input_array = OutputBar.number_textbox
            number_input_array.delete('1.0', tk.END)
                    
        text_value = "9"

        OutputBar.number_textbox.insert(tk.END, text_value) 

    def button_zeros(self):

        number_input_array = OutputBar.number_textbox
        number_input_array.delete('1.0', tk.END)

        text_value = "0"

        OutputBar.number_textbox.insert(tk.END, text_value)
        

    def a_c_button(self):
       
       number_input_array = OutputBar.number_textbox
       number_input_array.delete('1.0', tk.END)


    def add_buttons(self):
       
       number_input_array = OutputBar.number_textbox
       array_value = number_input_array.get('1.0', tk.END)
       global operation
       operation = '+'

       global variable_one
       variable_one = array_value

       number_input_array.delete('1.0', tk.END)
       
           
    def minus_buttons(self): 
       
       number_input_array = OutputBar.number_textbox
       array_value = number_input_array.get('1.0', tk.END)
       global operation
       operation = '-'

       global variable_one
       variable_one = array_value

       number_input_array.delete('1.0', tk.END)
        
    def times_buttons(self): 
    
       number_input_array = OutputBar.number_textbox
       array_value = number_input_array.get('1.0', tk.END)
       global operation
       operation = 'x'

       global variable_one
       variable_one = array_value

       number_input_array.delete('1.0', tk.END)

    def divide_buttons(self):
       
       number_input_array = OutputBar.number_textbox
       array_value = number_input_array.get('1.0', tk.END)
       global operation
       operation = '/'

       global variable_one
       variable_one = array_value

       number_input_array.delete('1.0', tk.END)

    def percentage_buttons(self):
        
        number_input_array = OutputBar.number_textbox
        array_value = number_input_array.get('1.0', tk.END)

        before_division = float(array_value)

        during_division = before_division / 100 

        after_division = str(during_division)

        global final_variable
        final_variable = after_division

        number_input_array.delete('1.0', tk.END)
        OutputBar.number_textbox.insert(tk.END, final_variable)

    def decimal_buttons(self): 

        #inserts after the value

        decimal_value = '.'

        OutputBar.number_textbox.insert(tk.END, decimal_value)        

    def negative_buttons(self): 

        number_input_array = OutputBar.number_textbox
        array_value = number_input_array.get('1.0', tk.END)
        number_input_array.delete('1.0', tk.END)

        negative_value = (int(array_value) - int(array_value)) - int(array_value) # value minuses three times to reach negative

        OutputBar.number_textbox.insert(tk.END, str(negative_value))

    def equal_buttons(self):
       
       number_input_array = OutputBar.number_textbox
       array_value = number_input_array.get('1.0', tk.END)

       global variable_two
       variable_two = array_value

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


       final_answer_value = str(final_variable)
       number_input_array.delete('1.0', tk.END)
       OutputBar.number_textbox.insert(tk.END, final_answer_value)
     

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
    button_zeroes = A.button_zeros
    ac_button = A.a_c_button
    add_button = A.add_buttons
    equal_button = A.equal_buttons
    times_button = A.times_buttons
    minus_buttonn = A.minus_buttons
    divide_buttonn = A.divide_buttons
    percentage_button = A.percentage_buttons 
    decimal_button = A.decimal_buttons
    negative_button = A.negative_buttons



    button_size = 30
    button_width = 6
    row_colour = 'Black'
    button_font_colour = 'White'


    button_frame = tk.Frame(calculator)
    button_frame.config(bg='White')
    button_frame.pack(side=tk.TOP, fill='x', expand=False)

    #row 1 

    row_one_frame = tk.Frame(button_frame)
    row_one_frame.config(bg=row_colour)
    row_one_frame.pack(side=tk.TOP, fill='x', expand=True)

    ac_button = tk.Button(row_one_frame, text='AC', font=button_size, width=button_width, command=ac_button)
    ac_button.grid(row=0, column=0, padx=10)

    plus_minus_button = tk.Button(row_one_frame, text='+/-', font=button_size, width=button_width, command=negative_button)
    plus_minus_button.grid(row=0, column=1, padx=10)

    percentage_button = tk.Button(row_one_frame, text='%', font=button_size, width=button_width, command=percentage_button)
    percentage_button.grid(row=0, column=2, padx=10)

    divide_button = tk.Button(row_one_frame, text='÷', bg='White', font=button_size, width=button_width, command=divide_buttonn)
    divide_button.grid(row=0, column=3, padx=10)

    #row 2

    row_two_frame = tk.Frame(button_frame)
    row_two_frame.config(bg=row_colour)
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
    row_three_frame.config(bg=row_colour)
    row_three_frame.pack(side=tk.TOP, fill='x', expand=False)

    four_button = tk.Button(row_three_frame, text='4', font=button_size, width=button_width, command=button_four)
    four_button.grid(row=2, column=0, padx=10, pady=2)

    five_button = tk.Button(row_three_frame, text='5', bg='White', font=button_size, width=button_width, command=button_five)
    five_button.grid(row=2, column=1, padx=10)

    six_button = tk.Button(row_three_frame, text='6', bg='White', font=button_size, width=button_width, command=button_six)
    six_button.grid(row=2, column=2, padx=10)

    minus_button = tk.Button(row_three_frame, text='-', bg='White', font=button_size, width=button_width, command=minus_buttonn)
    minus_button.grid(row=2, column=3, padx=10)

    #row 4
    row_four_frame =tk.Frame(button_frame)
    row_four_frame.config(bg=row_colour)
    row_four_frame.pack(side=tk.TOP, fill='x', expand=False)

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
    row_five_frame.config(bg=row_colour)
    row_five_frame.pack(side=tk.TOP, fill='x', expand=False)

    zero_button = tk.Button(row_four_frame, text='0', font=button_size, width=button_width, command=button_zeroes)
    zero_button.grid(row=4, column=0, padx=10, pady=2, columnspan=4)

    decimal_button = tk.Button(row_four_frame, text='.', font=button_size, width=button_width, command=decimal_button)
    decimal_button.grid(row=4, column=5, padx=10)

    equal_buttons = tk.Button(row_four_frame, text='=', bg='White', font=button_size, width=button_width, command=equal_button)
    equal_buttons.grid(row=4, column=6, padx=10)



Initialiser()
OutputBar()
Button()

calculator.mainloop()
