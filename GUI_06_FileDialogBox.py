from tkinter import filedialog
from tkinter import *
window=Tk()
window.title("EdGate Technologies")
window.geometry('350x200')

def submit():
    file = filedialog.askopenfilename(filetypes = (("Textfiles","*.txt"),("all files","*.*")))

btn=Button(window,text="Browse",command=submit)
btn.pack()
window.mainloop()