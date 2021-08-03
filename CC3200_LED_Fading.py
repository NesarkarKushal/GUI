from tkinter import *
import serial #pyserial 3.4
from serial import  *

window=Tk()
window.title("CC3200SF Microcontroller")
window.geometry("400x400")

comunication=serial.Serial('COM15',9600)

Horizontal= Scale(window,from_=0,to=255,orient=HORIZONTAL)
Horizontal.pack()

def click():
    value = Horizontal.get()
    put=str(value)
    data=put.encode()
    padding = 5
    # put=f"{value:#0{padding}x}"
    # enter='\\'+put
    comunication.write(data)

btn1 = Button(window, text="Clickk", command=click)
btn1.pack()

window.mainloop()
