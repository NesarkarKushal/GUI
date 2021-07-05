from tkinter import *
window=Tk()
global var
window.title("EdGate Technologies")
window.geometry('320x300')

# vertical=Scale(window,from_=0, to=100)
# vertical.pack()

Horizontal= Scale(window,from_=0,to=255,orient=HORIZONTAL)
Horizontal.pack()
def click():
    var = Horizontal.get()
    txt.delete(0, END)
    txt.insert(0,int(var))

btn1 = Button(window, text="Clickk", command=click)
btn1.pack()
txt=Entry(window,width=10)
txt.pack()
window.mainloop()