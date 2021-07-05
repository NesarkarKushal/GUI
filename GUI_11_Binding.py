from tkinter import *

window=Tk()
window.title("EdGate Technologies")
window.geometry("400x400")

def clicker(event=""):
    lbl=Label(window,text="Yes")  # event.Keysym,event.xchar
    lbl.pack()

btn=Button(window,text="Click")
btn.bind("<Button-1>",clicker) # Button-1 is left and middle button of mouse and Button-3 is right button of mouse
                                #Enter,Leave,FocusIn,FocousOut,Return=enter button fromkeyboard,Key

btn.pack(pady=20)

window.mainloop()
