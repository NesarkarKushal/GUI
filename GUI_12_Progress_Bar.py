
from tkinter import *

from tkinter.ttk import Progressbar

import time

from tkinter import ttk

window = Tk()

window.title("EdGate Technologies")

window.geometry('350x200')

# style = ttk.Style()
#
# style.theme_use('default')
# style.configure("black.Horizontal.TProgressbar", background='green')

bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar['value'] = 0
bar.pack()

def click():
    for i in range(0,110,10):
        bar['value'] = i
        window.update()
        time.sleep(1)



btn=Button(window,text="progress",command=click).pack()
window.mainloop()