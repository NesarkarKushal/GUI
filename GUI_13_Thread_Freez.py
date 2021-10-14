from tkinter import *
import time

window=Tk()
window.title("Training")
window.geometry('400x400')

def RED():
    time.sleep(5)
    window.config(bg="RED")


def orange():
    window.config(bg="Orange")


but=Button(window,text="RED",command=RED)
but.pack(pady=20)

but1=Button(window,text="ORANGE",command=orange)
but1.pack(pady=20)


window.mainloop()