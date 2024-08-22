import random as random 
import tkinter as tk

#universal value:
EMPTY_GRID_VALUE = '-'
FULL_GRID = '|-|-|-|\n|-|-|-|\n|-|-|-|'
LABEL_SEPERATOR = '|'
fonty = ('Times New Roman', 20)
bgg = 'Medium Slate Blue'


#gui part 
lee = tk.Tk()
lee.geometry("400x400")
lee.title("Tic Tac Toe")
lee.config(bg='Medium Slate Blue')


#constants for the tiles
empty_tile_1 = 0
empty_tile_2 = 0 
empty_tile_3 = 0 
empty_tile_4 = 0 
empty_tile_5 = 0 
empty_tile_6 = 0 
empty_tile_7 = 0 
empty_tile_8 = 0 
empty_tile_9 = 0 


def play_game():

    #constants for the game initialiser: 
    x_label = 0
    o_label = 0 
    O_button = False 
    x_button = False
    

    title_game_grame = tk.Frame(lee)
    title_game_grame.pack(side=tk.TOP, pady=5)

    game_frame = tk.Frame(lee, bg=bgg, bd=10)
    game_frame.pack(side=tk.TOP, pady=5)

    for widget in title_page_frame.winfo_children():
        widget.destroy()
    title_page_frame.destroy()

    #title above the game grid

    game_grid_title = tk.Label(title_game_grame, text='Game Grid', font=fonty, bg=bgg)
    game_grid_title.pack(side=tk.TOP)

    choose_character = tk.Label(lee, text='Choose Your Character', font=fonty, bg=bgg)
    choose_character.pack(side=tk.TOP)

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

    global empty_tile_1

    empty_tile_1 = tk.Button(game_frame, text=EMPTY_GRID_VALUE, font=fonty, command=grid_clicked_1)
    empty_tile_1.grid(row=0, column=1)

    global empty_tile_2

    empty_tile_2 = tk.Button(game_frame, text=EMPTY_GRID_VALUE, font=fonty, command=grid_clicked_2)
    empty_tile_2.grid(row=0, column=3)

    global empty_tile_3

    empty_tile_3 = tk.Button(game_frame, text=EMPTY_GRID_VALUE, font=fonty, command=grid_clicked_3)
    empty_tile_3.grid(row=0, column=5)

    #second line

    global empty_tile_4

    empty_tile_4 = tk.Button(game_frame, text=EMPTY_GRID_VALUE, font=fonty, command=grid_clicked_4)
    empty_tile_4.grid(row=1, column=1)

    global empty_tile_5

    empty_tile_5 = tk.Button(game_frame, text=EMPTY_GRID_VALUE, font=fonty, command=grid_clicked_5)
    empty_tile_5.grid(row=1, column=3)

    global empty_tile_6

    empty_tile_6 = tk.Button(game_frame, text=EMPTY_GRID_VALUE, font=fonty, command=grid_clicked_6)
    empty_tile_6.grid(row=1, column=5)

    

    #third line 

    global empty_tile_7

    empty_tile_7 = tk.Button(game_frame, text=EMPTY_GRID_VALUE, font=fonty, command=grid_clicked_7)
    empty_tile_7.grid(row=2, column=1)

    global empty_tile_8

    empty_tile_8 = tk.Button(game_frame, text=EMPTY_GRID_VALUE, font=fonty, command=grid_clicked_8)
    empty_tile_8.grid(row=2, column=3)

    global empty_tile_9

    empty_tile_9 = tk.Button(game_frame, text=EMPTY_GRID_VALUE, font=fonty, command=grid_clicked_9)
    empty_tile_9.grid(row=2, column=5)

    player_frame = tk.Frame(lee, bg=bgg)
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

#win conditions
#horizontal -> 1,2,3  4,5,6,  7,8,9 (vice versa)
#vertical -> 1,4,7  2,5,8,  3,6,9 
#diagonal -> 1,5,9  3,5,7 

    def clear():
        global empty_tile_1
        global empty_tile_2
        global empty_tile_3
        global empty_tile_4
        global empty_tile_5
        global empty_tile_6
        global empty_tile_7
        global empty_tile_8
        global empty_tile_9

        empty_tile_1.config(text=EMPTY_GRID_VALUE)
        empty_tile_2.config(text=EMPTY_GRID_VALUE)
        empty_tile_3.config(text=EMPTY_GRID_VALUE)
        empty_tile_4.config(text=EMPTY_GRID_VALUE)
        empty_tile_5.config(text=EMPTY_GRID_VALUE)
        empty_tile_6.config(text=EMPTY_GRID_VALUE)
        empty_tile_7.config(text=EMPTY_GRID_VALUE)
        empty_tile_8.config(text=EMPTY_GRID_VALUE)
        empty_tile_9.config(text=EMPTY_GRID_VALUE)


    choose_x_o = tk.Button(player_frame, text='X', font=fonty, command=x_clicked, bg=bgg)
    choose_x_o.grid(row=4, column=0, columnspan=2, pady=5)

    choose_o_x = tk.Button(player_frame, text='O', font=fonty, command=o_clicked, bg=bgg)
    choose_o_x.grid(row=4, column=4, columnspan=2, pady=5)

    clear_button = tk.Button(lee, text='Clear', font=('Arial', 16), command=clear, bg=bgg)
    clear_button.pack(side=tk.TOP)




    
    
#outside frames and buttons

title_page_frame = tk.Frame(lee, bg=bgg)
title_page_frame.pack(side=tk.TOP)

title_label = tk.Label(title_page_frame, text='Tic Tac Toe Game', font=('Arial', 30), bg=bgg, fg='White')
title_label.pack(side=tk.TOP, pady=20)

play_button = tk.Button(title_page_frame, text='Play Game', font=('Arial', 30), bg=bgg, command=play_game, fg='White')
play_button.pack(side=tk.TOP, pady=20)


lee.mainloop()
