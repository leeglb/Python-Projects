import random as random 
import tkinter as tk

#universal value:
EMPTY_GRID_VALUE = '-'
FULL_GRID = '|-|-|-|\n|-|-|-|\n|-|-|-|'
LABEL_SEPERATOR = '|'

#gui part 
lee = tk.Tk()
lee.geometry("500x500")
lee.title("Tic Tac Toe")
lee.config(bg='Blue')

#constants for gui
fonty = ('Arial', 20)


def play_game():

    #constants for the game initialiser: 
    x_label = 0
    o_label = 0 
    O_button = False 
    x_button = False
    

    title_game_grame = tk.Frame(lee)
    title_game_grame.pack(side=tk.TOP, pady=5)

    game_frame = tk.Frame(lee, bg='Blue', bd=10)
    game_frame.pack(side=tk.TOP, pady=5)

    for widget in title_page_frame.winfo_children():
        widget.destroy()
    title_page_frame.destroy()

    #title above the game grid

    game_grid_title = tk.Label(title_game_grame, text='Game Grid', font=fonty)
    game_grid_title.pack(side=tk.TOP)

    def grid_clicked_1():
        button_clicked = True 

        if button_clicked == True:

            global x_button
            global O_button

            if x_button == True:
                empty_tile_1.config(text='X')
            
            elif O_button == True:
                empty_tile_1.config(text='O')
        
    def grid_clicked_2():
        button_clicked = True 
        if button_clicked == True:

            global x_button
            global O_button

            if x_button is True:
                empty_tile_2.config(text='X')

            elif O_button == True:
                empty_tile_2.config(text='O')
        
    def grid_clicked_3():
        button_clicked = True 
        if button_clicked == True:

            global x_button
            global O_button

            if x_button == True:
                empty_tile_3.config(text='X')

            elif O_button == True:
                empty_tile_3.config(text='O')

    def grid_clicked_4():
        button_clicked = True 
        if button_clicked == True:

            global x_button
            global O_button

            if x_button == True:
                empty_tile_4.config(text='X')
            elif O_button == True:
                empty_tile_4.config(text='O')
    
    def grid_clicked_5():
        button_clicked = True 
        if button_clicked == True:

            global x_button
            global O_button

            if x_button == True:
                empty_tile_5.config(text='X')
            elif O_button == True:
                empty_tile_5.config(text='O')

    def grid_clicked_6():
        button_clicked = True 
        if button_clicked == True:

            global x_button
            global O_button

            if x_button == True:
                empty_tile_6.config(text='X')
            elif O_button == True:
                empty_tile_6.config(text='O')

    def grid_clicked_7():
        button_clicked = True 
        if button_clicked == True:

            global x_button
            global O_button

            if x_button == True:
                empty_tile_7.config(text='X')
            elif O_button == True:
                empty_tile_7.config(text='O')

    def grid_clicked_8():
        button_clicked = True 
        if button_clicked == True:

            global x_button
            global O_button

            if x_button == True:
                empty_tile_8.config(text='X')
            elif O_button == True:
                empty_tile_8.config(text='O')
        
    def grid_clicked_9():
        button_clicked = True 
        if button_clicked == True:

            global x_button
            global O_button

            if x_button == True:
                empty_tile_9.config(text='X')

            elif O_button == True:
                empty_tile_9.config(text='O')

    #first line

    line_seperator_0 = tk.Label(game_frame, text=LABEL_SEPERATOR, font=fonty)
    line_seperator_0.grid(row=0, column=0)

    empty_tile_1 = tk.Button(game_frame, text=EMPTY_GRID_VALUE, font=fonty, command=grid_clicked_1)
    empty_tile_1.grid(row=0, column=1)

    line_seperator_1 = tk.Label(game_frame, text=LABEL_SEPERATOR, font=fonty)
    line_seperator_1.grid(row=0, column=2)

    empty_tile_2 = tk.Button(game_frame, text=EMPTY_GRID_VALUE, font=fonty, command=grid_clicked_2)
    empty_tile_2.grid(row=0, column=3)

    line_seperator_2 = tk.Label(game_frame, text=LABEL_SEPERATOR, font=fonty)
    line_seperator_2.grid(row=0, column=4)

    empty_tile_3 = tk.Button(game_frame, text=EMPTY_GRID_VALUE, font=fonty, command=grid_clicked_3)
    empty_tile_3.grid(row=0, column=5)

    line_seperator_3 = tk.Label(game_frame, text=LABEL_SEPERATOR, font=fonty)
    line_seperator_3.grid(row=0, column=6)

    #second line

    line_seperator_4 = tk.Label(game_frame, text=LABEL_SEPERATOR, font=fonty)
    line_seperator_4.grid(row=1, column=0)

    empty_tile_4 = tk.Button(game_frame, text=EMPTY_GRID_VALUE, font=fonty, command=grid_clicked_4)
    empty_tile_4.grid(row=1, column=1)

    line_seperator_5 = tk.Label(game_frame, text=LABEL_SEPERATOR, font=fonty)
    line_seperator_5.grid(row=1, column=2)

    empty_tile_5 = tk.Button(game_frame, text=EMPTY_GRID_VALUE, font=fonty, command=grid_clicked_5)
    empty_tile_5.grid(row=1, column=3)

    line_seperator_6 = tk.Label(game_frame, text=LABEL_SEPERATOR, font=fonty)
    line_seperator_6.grid(row=1, column=4)

    empty_tile_6 = tk.Button(game_frame, text=EMPTY_GRID_VALUE, font=fonty, command=grid_clicked_6)
    empty_tile_6.grid(row=1, column=5)

    line_seperator_7 = tk.Label(game_frame, text=LABEL_SEPERATOR, font=fonty)
    line_seperator_7.grid(row=1, column=6)

    #third line 

    line_seperator_8 = tk.Label(game_frame, text=LABEL_SEPERATOR, font=fonty)
    line_seperator_8.grid(row=2, column=0)

    empty_tile_7 = tk.Button(game_frame, text=EMPTY_GRID_VALUE, font=fonty, command=grid_clicked_7)
    empty_tile_7.grid(row=2, column=1)

    line_seperator_9 = tk.Label(game_frame, text=LABEL_SEPERATOR, font=fonty)
    line_seperator_9.grid(row=2, column=2)

    empty_tile_8 = tk.Button(game_frame, text=EMPTY_GRID_VALUE, font=fonty, command=grid_clicked_8)
    empty_tile_8.grid(row=2, column=3)

    line_seperator_10 = tk.Label(game_frame, text=LABEL_SEPERATOR, font=fonty)
    line_seperator_10.grid(row=2, column=4)

    empty_tile_9 = tk.Button(game_frame, text=EMPTY_GRID_VALUE, font=fonty, command=grid_clicked_9)
    empty_tile_9.grid(row=2, column=5)

    line_seperator_11 = tk.Label(game_frame, text=LABEL_SEPERATOR, font=fonty)
    line_seperator_11.grid(row=2, column=6)

    player_frame = tk.Frame(lee)
    player_frame.pack(side=tk.TOP, pady=5)
    

    def x_clicked():

        global x_button
        x_button = True

        global O_button
        O_button = False 

    def o_clicked():

        global O_button
        O_button = True

        global x_button 
        x_button = False  


    choose_x_o = tk.Button(player_frame, text='X', font=fonty, command=x_clicked)
    choose_x_o.grid(row=4, column=0, columnspan=2, pady=5)

    choose_o_x = tk.Button(player_frame, text='O', font=fonty, command=o_clicked)
    choose_o_x.grid(row=4, column=4, columnspan=2, pady=5)

    choose_character = tk.Label(lee, text='Choose Your Character', font=fonty)
    choose_character.pack(side=tk.TOP)

#win conditions
#horizontal -> 1,2,3  4,5,6,  7,8,9 (vice versa)
#vertical -> 1,4,7  2,5,8,  3,6,9 
#diagonal -> 1,5,9  3,5,7 
def win_condition():
    global x_button
    if x_button is True:
        x_list = []

        a = empty_tile_1.cget('text') 
        b = empty_tile_2.cget('text') 
        c = empty_tile_3.cget('text')

        x_list.append(a,b,c)
        for value in x_list:
            if value == 'X':
                win_label = tk.Label(lee, text='You Won!', font=fonty)
                win_label.pack(side=tk.TOP)






title_page_frame = tk.Frame(lee, bg='Blue')
title_page_frame.pack(side=tk.TOP)

title_label = tk.Label(title_page_frame, text='Tic Tac Toe Game', font=('Arial', 30), bg='Black', fg='White')
title_label.pack(side=tk.TOP)

play_button = tk.Button(title_page_frame, text='Play Game', font=('Arial', 30), bg='White', command=play_game)
play_button.pack(side=tk.TOP, pady=20)



lee.mainloop()




