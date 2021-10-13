from tkinter import *
from tkinter import colorchooser

window=Tk()
window.title("Edgate Technologies")
window.geometry("400x400")

def color():
    var=colorchooser.askcolor(title="Choose color")
    for i in var:
        print(i)

    window.configure(bg=i)

button=Button(window,text="Click",command=color).grid()

window.mainloop()