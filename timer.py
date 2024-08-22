import tkinter as tk
import time as time
import random as random

lee = tk.Tk()
lee.geometry("300x300")
lee.title("Timer")


title_label = tk.Label(lee, text='Timer', font=('Times New Roman', 20), bg='Light Blue')
title_label.pack(side=tk.TOP)

def timer():
     
    start_time = time.time()

    count = int(timer_text.get("1.0", "end"))

    time.sleep(count)

    end_time = time.time()

    elapsed_time = end_time - start_time 

    time_check = elapsed_time 

    if time_check == elapsed_time: 

        timer_output = tk.Label(lee, text='Times Up', bg='Light Blue')

        timer_output.pack(side=tk.TOP)

        colour_list = ['yellow', 'red', 'blue', 'green', 'pink']

        random_color = random.choice(colour_list)

        lee.config(bg=random_color)

timer_text = tk.Text(lee, height=2, width=10, bg='Light Blue')
timer_text.pack(side=tk.TOP, pady=20)

timer_button = tk.Button(lee, text='COUNT DOWN!', bg='Light Blue', command=timer)
timer_button.pack(side=tk.TOP, pady=20)

def clear():
    pass 

clear_button = tk.Button(lee, text='Clear', bg='Light Blue', command=clear)
    

    
lee.mainloop()