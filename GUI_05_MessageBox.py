from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("EdGate Technologies")
window.geometry('350x200')
def clicked():
    # messagebox.showinfo('Message title', 'Successfully clicked')
    #messagebox.showwarning('Message title', 'Warning')
    messagebox.showerror('Message title', 'Somethingwent wrong') # shows error message

btn = Button(window,text='Click here', command=clicked)
btn.grid(column=0,row=0)
window.mainloop()