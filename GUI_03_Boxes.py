from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
window = Tk()
window.geometry('400x400')
window.title("welcome")

combo=Combobox(window)
combo['values']=(1,2,3,4,5,"Text")
combo.current(5)
combo.pack()

chk_state=IntVar()
chk_state.set(1)
chk=Checkbutton(window,text='Choose',var=chk_state)
chk.pack()

rad1=Radiobutton(window,text='one',value=1)
rad1.pack()

rad2=Radiobutton(window,text='two',value=2)
rad2.pack()

rad3=Radiobutton(window,text='six',value=3)
rad3.pack()

spin = Spinbox(window, from_=0, to=100, width=5)
spin.pack()

txt = scrolledtext.ScrolledText(window,width=40,height=10)
txt.insert(INSERT,'You can put any Details here\n')

txt.pack()
 
window.mainloop()
