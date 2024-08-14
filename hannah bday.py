import tkinter as tk
from PIL import Image, ImageTk


lee = tk.Tk()
lee.title('Happy Bday Hannah')
lee.geometry("600x600")
lee.config(bg='Pink')

def press_me():
    lee.config(bg='Pink')
    happy_birthday_button.destroy() and happy_birthday_label.destroy()
    canvas.destroy()
    text_label = tk.Label(text="Hannah, thank you for being my friend for the time I've known you\nI have enjoyed every moment being with you\nand you are the most amazing and cool person to ever exist", bg='Pink')
    text_label.pack()
    text_later_label = tk.Label(text='I will text you my huge amazing paragraph right after i send this hehe\nTHANK YOU I WANTED TO TRY MAKE SOMETHING CUTE USING CODE\nIT AINT AMAZING BUT IM LEARNING\nRAHHHHH', bg='Pink')
    text_later_label.pack(pady=10)

    happy_birthday_label = tk.Label(text='HAPPY FUCKING BDAY!!!!', font=('Arial', 40), bg='Pink')
    happy_birthday_label.pack(pady=10)

happy_birthday_label = tk.Label(lee, text='Happy Birthday!', font=('Arial', 16))
happy_birthday_label.pack(side=tk.TOP, pady=10)

happy_birthday_button = tk.Button(lee, text='Press Me :)', font=('Arial', 16), command=press_me)
happy_birthday_button.pack(side=tk.TOP)

canvas = tk.Canvas(lee, width=600, height=600)
canvas.pack(fill=tk.BOTH, expand=True)


image_path = "/Users/galbraithlee/Downloads/bday.jpg"
image1 = Image.open(image_path)


canvas_width = 600
canvas_height = 600

image1.thumbnail((canvas_width, canvas_height), Image.LANCZOS)


images = ImageTk.PhotoImage(image1)


image_width, image_height = image1.size
x = (canvas_width - image_width) // 2
y = (canvas_height - image_height) // 2


canvas.create_image(x, y, anchor=tk.NW, image=images)


lee.mainloop()
