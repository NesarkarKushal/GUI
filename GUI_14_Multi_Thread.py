from tkinter import *
import time
import threading
# from threading import  Thread

window=Tk()
window.title("Hello")
window.geometry('400x400')

def RED():
    time.sleep(5)
    window.config(bg="RED")

def ORANGE():
    time.sleep(2)
    window.config(bg="ORANGE")

def BLUE():
    time.sleep(1)
    window.config(bg="BLUE")

but=Button(window,text="RED",command=threading.Thread(target=RED).start)
but.pack(pady=20)

but1=Button(window,text="ORANGE",command=threading.Thread(target=ORANGE).start)
but1.pack(pady=20)
but2=Button(window,text="BLUE",command=threading.Thread(target=BLUE).start)
but2.pack(pady=20)

window.mainloop()