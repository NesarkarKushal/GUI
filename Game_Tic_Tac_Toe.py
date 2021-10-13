from tkinter import *
from tkinter import messagebox

window= Tk()
window.title("Edgate Technologies")

global var,a,b,c,d,e,f,g,h,i,dr
var,a,b,c,d,e,f,g,h,i,dr="O","a","k","b","z","p","c","w","p","j",0

def click0():
    global  var,a
    if var =="O":
        butt0.configure(text="X")
        var,a="X","X"
    elif var=="X":
        butt0.configure(text="O")
        var,a="O","O"

def click1():
    global var,b
    if var == "O":
        butt1.configure(text="X")
        var,b= "X","X"
    elif var == "X":
        butt1.configure(text="O")
        var,b = "O","O"

def click2():
    global var,c
    if var == "O":
        butt2.configure(text="X")
        var,c= "X","X"
    elif var == "X":
        butt2.configure(text="O")
        var,c= "O","O"

def click3():
    global var,d
    if var == "O":
        butt3.configure(text="X")
        var, d = "X", "X"
    elif var == "X":
        butt3.configure(text="O")
        var ,d = "O","O"

def click4():
    global  var,e
    if var =="O":
        butt4.configure(text="X")
        var,e="X","X"
    elif var=="X":
        butt4.configure(text="O")
        var,e="O","O"

def click5():
    global var,f
    if var == "O":
        butt5.configure(text="X")
        var ,f= "X","X"
    elif var == "X":
        butt5.configure(text="O")
        var ,f= "O","O"

def click6():
    global var,g
    if var == "O":
        butt6.configure(text="X")
        var ,g= "X","X"
    elif var == "X":
        butt6.configure(text="O")
        var ,g= "O","O"

def click7():
    global var,h
    if var == "O":
        butt7.configure(text="X")
        var ,h= "X","X"
    elif var == "X":
        butt7.configure(text="O")
        var ,h= "O","O"

def click8():
    global var,i
    if var == "O":
        butt8.configure(text="X")
        var ,i= "X","X"
    elif var == "X":
        butt8.configure(text="O")
        var ,i= "O","O"

def ref():
    butt0.configure(text=" ",bg="gray")
    butt1.configure(text=" ",bg="gray")
    butt2.configure(text=" ",bg="gray")
    butt3.configure(text=" ",bg="gray")
    butt4.configure(text=" ",bg="gray")
    butt5.configure(text=" ",bg="gray")
    butt6.configure(text=" ",bg="gray")
    butt7.configure(text=" ",bg="gray")
    butt8.configure(text=" ",bg="gray")

def res():
    if a == " X":
        if b =="X":
            if c== "X":
                butt0.configure(bg="red")
                butt1.configure(bg="red")
                butt2.configure(bg="red")
            else:
                pass
        else:
            pass
    else:
        pass


    if a == "O":
         if b== "O":
             if c== "O":
                 butt0.configure(bg="red")
                 butt1.configure(bg="red")
                 butt2.configure(bg="red")
             else:
                 pass
         else:
             pass
    else:
        pass

    if d == "X":
        if e == "X":
            if f == "X":
                butt3.configure(bg="red")
                butt4.configure(bg="red")
                butt5.configure(bg="red")
            else:
                pass
        else:
            pass
    else:
        pass

    if d == "O":
        if e == "O":
            if f == "O":
                butt3.configure(bg="red")
                butt4.configure(bg="red")
                butt5.configure(bg="red")
            else:
                pass
        else:
            pass
    else:
        pass

    if g == "X":
        if h == "X":
            if i == "X":
                butt6.configure(bg="red")
                butt7.configure(bg="red")
                butt8.configure(bg="red")
            else:
                pass
        else:
            pass
    else:
        pass

    if g == "O":
        if h == "O":
            if i == "O":
                butt6.configure(bg="red")
                butt7.configure(bg="red")
                butt8.configure(bg="red")
            else:
                pass
        else:
            pass
    else:
        pass

    if a == "X":
        if d == "X":
            if g == "X":
                butt0.configure(bg="red")
                butt3.configure(bg="red")
                butt6.configure(bg="red")
            else:
                pass
        else:
            pass
    else:
        pass

    if a == "O":
        if d == "O":
            if g == "O":
                butt0.configure(bg="red")
                butt3.configure(bg="red")
                butt6.configure(bg="red")
            else:
                pass
        else:
            pass
    else:
        pass

    if b == "X":
        if e == "X":
            if h == "X":
                butt1.configure(bg="red")
                butt4.configure(bg="red")
                butt7.configure(bg="red")
                return 0
            else:
                pass
        else:
            pass
    else:
        pass

    if b == "O":
        if e == "O":
            if h == "O":
                butt1.configure(bg="red")
                butt4.configure(bg="red")
                butt7.configure(bg="red")
                return 0
            else:
                pass
        else:
            pass
    else:
        pass


    if c == "X":
        if f == "X":
            if i == "X":
                butt2.configure(bg="red")
                butt5.configure(bg="red")
                butt8.configure(bg="red")
            else:
                pass
        else:
            pass
    else:
        pass

    if c == "O":
        if f == "O":
            if i == "O":
                butt2.configure(bg="red")
                butt5.configure(bg="red")
                butt8.configure(bg="red")
            else:
                pass
        else:
            pass
    else:
        pass

    if a == "X":
        if e == "X":
            if i == "X":
                butt0.configure(bg="red")
                butt4.configure(bg="red")
                butt8.configure(bg="red")
            else:
                pass
        else:
            pass
    else:
        pass

    if a == "O":
        if e == "O":
            if i == "O":
                butt0.configure(bg="red")
                butt4.configure(bg="red")
                butt8.configure(bg="red")
            else:
                pass
        else:
            pass
    else:
        pass

    if c == "X":
        if e == "X":
            if g == "X":
                butt2.configure(bg="red")
                butt4.configure(bg="red")
                butt6.configure(bg="red")
    else:
        pass

    if c == "O":
        if e == "O":
            if g == "O":
                butt2.configure(bg="red")
                butt4.configure(bg="red")
                butt6.configure(bg="red")

    # else:
    #     global dr
    #     dr=1
    #
    # if dr != 1:
    #     messagebox.showinfo('Status', 'Match Draw')


butt0=Button(window,text=" ",font=("TimeNewRoman",20),height=3,width=6,command=click0)
butt1=Button(window,text=" ",font=("TimeNewRoman",20),height=3,width=6,command=click1)
butt2=Button(window,text=" ",font=("TimeNewRoman",20),height=3,width=6,command=click2)
butt3=Button(window,text=" ",font=("TimeNewRoman",20),height=3,width=6,command=click3)
butt4=Button(window,text=" ",font=("TimeNewRoman",20),height=3,width=6,command=click4)
butt5=Button(window,text=" ",font=("TimeNewRoman",20),height=3,width=6,command=click5)
butt6=Button(window,text=" ",font=("TimeNewRoman",20),height=3,width=6,command=click6)
butt7=Button(window,text=" ",font=("TimeNewRoman",20),height=3,width=6,command=click7)
butt8=Button(window,text=" ",font=("TimeNewRoman",20),height=3,width=6,command=click8)

butt0.grid(row=0,column=1)
butt1.grid(row=0,column=2)
butt2.grid(row=0,column=3)
butt3.grid(row=1,column=1)
butt4.grid(row=1,column=2)
butt5.grid(row=1,column=3)
butt6.grid(row=2,column=1)
butt7.grid(row=2,column=2)
butt8.grid(row=2,column=3)

result= Button(window,text="Result",command=res)
result.grid(row=3,column=1)

Refresh= Button(window,text="Refresh",command=ref)
Refresh.grid(row=3,column=2)

window.mainloop()