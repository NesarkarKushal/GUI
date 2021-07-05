from tkinter import  *
import time
import threading

window=Tk()
window.title("EdGate Technologies")
window.geometry("500x200")
window.configure(bg="Black")

global min,hrs,sec,b
min,hrs,sec=0,0,0

def setting():
    global min,hrs

    win1=Toplevel()
    win1.geometry("200x140")
    win1.title("Setting")
    lab=Label(win1,text="Select Hour")
    lab.place(x=10,y=10)
    spin = Spinbox(win1, from_=0, to=23, width=5)
    spin.place(x=80,y=10)

    lab1= Label(win1, text="Select min")
    lab1.place(x=10, y=50)
    spin1 = Spinbox(win1, from_=0, to=59, width=5)
    spin1.place(x=80, y=50)

    def selected():
        global hrs, min
        # hrs = spin.get()
        # min = spin1.get()

        hrs=int(spin.get())
        min=int(spin1.get())

        lbl0.configure(text=hrs)
        lbl2.configure(text=min)

    btn0 = Button(win1, text="ok", command=selected)
    btn0.place(x=130, y=10)
    btn1 = Button(win1, text="ok", command=selected)
    btn1.place(x=130, y=50)

def start():
    global sec,min,hrs

    while 1:
        for a in range(1, 60):
            sec = a
            lbl4.configure(text=sec)
            time.sleep(1)


            if sec == 59:
                min += 1
                lbl2.configure(text=min)
            if min == 59:
                hrs += 1
                lbl0.configure(text=hrs)

lbl0=Label(window,text="0",font=("Arial, Bold",14),width=5,bg="Black",fg="white")
lbl0.place(x=80,y=10)
lbl1=Label(window,text=".",font=("Arial, Bold",30),bg="Black",fg="white").place(x=152,y=10)

lbl2=Label(window,text="0",font=("Arial, Bold",14),width=5,bg="Black",fg="white")
lbl2.place(x=175,y=10)
lbl3=Label(window,text=".",font=("Arial, Bold",30),bg="Black",fg="white").place(x=250,y=10,)

lbl4=Label(window,text="0",font=("Arial, Bold",14),width=5,bg="Black",fg="white")
lbl4.place(x=270,y=10)

lbl5=Label(window,text="Hrs",font=("Arial, Bold",15),bg="Black",fg="white").place(x=90,y=50)
lbl6=Label(window,text="Min",font=("Arial, Bold",15),bg="Black",fg="white").place(x=185,y=50)
lbl7=Label(window,text="Sec",font=("Arial, Bold",15),bg="Black",fg="white").place(x=280,y=50)

btn2=Button(window,text="Start",font=("Arial, Bold",14),width=8,bg="Black",fg="white",command=threading.Thread(target=start).start)
btn2.place(x=100,y=100)
btn3=Button(window,text="Setting",font=("Arial, Bold",14),width=8,bg="Black",fg="white",command=threading.Thread(target=setting).start)
btn3.place(x=235,y=100)

window.mainloop()