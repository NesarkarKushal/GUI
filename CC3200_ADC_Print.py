from tkinter import *
import serial
import time
import threading

window=Tk()
window.title("Monitor The ADC Value")
window.geometry("400x400")
window.configure(bg="light blue")


ser=serial.Serial('COM15',9600)


def start():
    while 1:
        data = ser.readline()
        a = data.decode()
        txt.insert(INSERT, a)
        time.sleep(1)
        txt.delete(0, END)


but=Button(window,text="Start",command=threading.Thread(target=start).start)
but.place(x=180,y=60,width=60,height=30)

txt = Entry(window, width=20)
txt.place(x=150,y=100,height=30)


window.mainloop()