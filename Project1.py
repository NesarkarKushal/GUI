from tkinter import *
from PIL import ImageTk,Image
import  webbrowser

window=Tk()
window.geometry('350x180')
window.title("EdGate Technologies")

Load=Image.open("E:\\GUI Folder\\download.jpg")
my_image=ImageTk.PhotoImage(Load)
img=Label(window,image=my_image)
img.image=my_image
img.pack()

window=mainloop()