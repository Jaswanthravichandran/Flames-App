from cProfile import label
import tkinter as tk
from PIL import Image,ImageTk


root = tk.Tk()

canvas = tk.Canvas(root,width=800, height=400)

canvas.grid(columnspan=3)
logo = Image.open('icon.png')
logo = ImageTk.PhotoImage(logo)
lable_logo = tk.Label(image=logo)
lable_logo.image = logo 
lable_logo.grid(column=1,row=0)
root.mainloop()