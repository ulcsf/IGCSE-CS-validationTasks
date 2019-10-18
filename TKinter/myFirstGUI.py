# ***********************************************
#    My First GUI project
# ***********************************************

from tkinter import *

window = Tk()
window.title("Welcome to my 1st GUI app")

lbl = Label(window, text="Hello")
#lbl.grid(column=0, row=0)
lbl.pack()


def clicked():
    lbl.configure(text="Button was clicked !!")
    


btn = Button(window, text="Click Me", command=clicked)
#btn.grid(column=1, row=1)

#
window.mainloop()

