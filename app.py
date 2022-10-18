from cProfile import label
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import *

root = tk.Tk()

root.geometry("400x250")  

#canvas = tk.Canvas(root,width=800, height=400)

#canvas.grid(columnspan=3)

your_name = Label(root,text="Your Name")#.place(x=80,y=90)
your_name.pack(side=LEFT)
partner_name = Label(root,text="Partner Name").place(x=80,y=160)
#e1 = Entry(root).side()  
e2 = Entry(root).place(x = 190, y = 160)  
# logo = Image.open('icon.png')
# logo = ImageTk.PhotoImage(logo)
# lable_logo = tk.Label(image=logo)
# lable_logo.image = logo 
# lable_logo.grid(column=1,row=0)
root.mainloop()