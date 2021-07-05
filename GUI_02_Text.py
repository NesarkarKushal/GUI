
from tkinter import *


#-------------- creating a window -------------
window = Tk()
window.geometry('300x300')
window.title("EdGate Technologies")

# -------------- Lable in window ---------------------

lbl=Label(window,text="Hello",font=("TimesNewRoman Bold",15))
lbl.pack()

#--------------- Input Using Entry class --------------
txt= Entry(window,width=20)
txt.pack()
txt.focus()

# -------------- Disable Entry Widget -----------------
# txt=Entry(window,width=10,state='disabled')
# txt.grid()

#-------------- Handle button click event-----------------------

def clicked():
    res="Welcome " + txt.get()
    lbl.configure(text=res,bg="yellow")


btn=Button(window,text="Submit",command=clicked)
btn.pack()


window.mainloop()

