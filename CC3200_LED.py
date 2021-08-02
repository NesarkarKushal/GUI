from tkinter import *
import serial #pyserial 3.4
from serial import  *

window=Tk()
window.title("CC3200SF Microcontroller")
window.geometry("400x400")

comunication=serial.Serial('COM15',9600)

def Ron():
    comunication.write(b'r')

def Gon():
    comunication.write(b'g')

def Bon():
    comunication.write(b'b')


btn=Button(window,text="RED",bg="red",command=Ron)
btn.pack(fill=X)

btn=Button(window,text="GREEN",bg="light Green",command=Gon)
btn.pack(fill=X)

btn=Button(window,text="Yellow",bg="Yellow",command=Bon)
btn.pack(fill=X)


window.mainloop()