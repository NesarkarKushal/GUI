from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry('320x320')
window.title("EdGate Technologies")

tab_control = ttk.Notebook(window)

#----------- Page one --------------

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='First')
tab_control.pack(expand=1, fill='both')
lbl=Label(tab1,text="Hi How are You")
lbl.grid(column=0, row=0,padx=5)

#----------- Page 2 --------------

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='second')
tab_control.pack(expand=1, fill='both') # pack to make visible
lbl1=Label(tab2,text="Enter age")
lbl1.grid(column=0, row=0,padx=5)

window.mainloop()