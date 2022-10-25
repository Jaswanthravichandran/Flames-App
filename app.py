from tkinter import *
from api import *


def submit():
    username = entry.get()
    print(username)

window = Tk()

window.geometry("480x420")

window.title("Flames Game")

icon = PhotoImage(file="icon.png")

window.iconphoto(True,icon)

window.config(background="#e6a39a")

label = Label(window,
text="Find Your Partner",
font=('times new roman',20),
fg='#00FF00',
bg='black',
padx=20,
pady=20)

entry = Entry(window,font=('Arial',20))

entry.pack(padx=25,pady=10)


button = Button(window,
text="Submit",
command=submit,
font=('Comic Sans',15),)

button.pack(side=RIGHT)



label.pack()

window.mainloop()