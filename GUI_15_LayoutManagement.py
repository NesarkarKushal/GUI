from tkinter import *

window=Tk()
window.title("EdGate Technologies")
window.geometry('320x320')

# -----------------Frame 1------------------------

lbl_frame= LabelFrame(window,text="")
lbl_frame.place(x=50,y=50)
lbl=Label(lbl_frame,text="Enter Name")
lbl.grid(column=0, row=0,padx=5)
txt= Entry(lbl_frame,width=10)
txt.grid(column=1, row=0,padx=5)
txt.focus()
but=Button(lbl_frame,text="click me")
but.grid(column=2, row=0,padx=5)

#------------------ Frame 2 --------------------------
lbl_frame1=LabelFrame(lbl_frame,text="page")
lbl_frame1.grid(column=0, row=1,padx=5)
lbl1=Label(lbl_frame1,text="Enter Age")
lbl1.grid(column=0, row=2,pady=5)
txt1= Entry(lbl_frame1,width=10)
txt1.grid(column=0, row=3,pady=5)
txt1.focus()
but1=Button(lbl_frame1,text="click me")
but1.grid(column=0, row=4,pady=5)

window=mainloop()