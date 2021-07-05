from tkinter import *

window=Tk()
window.geometry('275x300')
window.title("EdGate Technologies")

txt=Entry(window,width=32,bd=8,font=("TimesNewRoman Bold",8))
txt.grid(column=0, row=0,columnspan=30,ipadx=20,ipady=10,padx=4,pady=4)


def click(num):
    # txt.delete(0,END)
    current=txt.get()
    txt.delete(0,END)
    txt.insert(0,str(current) + str(num))
    return

def clear():
    txt.delete(0,END)

def add():
    one1=txt.get()
    global a,b,c,d,e
    a=int(one1)
    b=" "
    c=" "
    d=" "
    e=" "
    txt.delete(0,END)

def sub():
    one1=txt.get()
    global b,a,c,d,e
    a=" "
    b=int(one1)
    c=" "
    d=" "
    e=" "
    txt.delete(0,END)

def mul():
    one1=txt.get()
    global a, b, c, d ,e
    a=" "
    b=" "
    c=int(one1)
    d=" "
    e=" "
    txt.delete(0,END)

def div():
    one1=txt.get()
    global a, b, c, d ,e
    a=" "
    b=" "
    c=" "
    d=int(one1)
    e=" "
    txt.delete(0,END)

def mod():
    one1=txt.get()
    global a, b, c, d ,e
    a=" "
    b=" "
    c=" "
    d=" "
    e=int(one1)
    txt.delete(0,END)

def equal():
    two=txt.get()
    txt.delete(0,END)
    if a != " ":
        txt.insert(0, a + int(two))
    else:
        pass
    if b != " ":
        txt.insert(0, b - int(two))
    else:
        pass

    if c != " ":
        txt.insert(0, c * int(two))
    else:
        pass

    if d != " ":
        txt.insert(0, d / int(two))
    else:
        pass

    if e != " ":
        txt.insert(0, e % int(two))
    else:
        pass

def dele():
    txt.delete(0,1)


#

btnc=Button(window,text="c",height=2,width=8,bg='light blue',command=clear)
btnM=Button(window,text="%",height=2,width=8,bg='light blue',command=mod)
btndd=Button(window,text="del",padx=3,pady=3,bg='light blue',height=2,width=8,command=dele)
btnd=Button(window,text="/",padx=3,pady=3,bg='light blue',height=2,width=8,command=div)
#

btn7=Button(window,text="7",height=2,width=8,bg='light blue',command=lambda:click(7))
btn8=Button(window,text="8",height=2,width=8,bg='light blue',command=lambda:click(8))
btn9=Button(window,text="9",height=2,width=8,bg='light blue',command=lambda:click(9))
btnm=Button(window,text="*",height=2,width=8,bg='light blue',command=mul)


btn4=Button(window,text="4",height=2,width=8,bg='light blue',command=lambda:click(4))
btn5=Button(window,text="5",height=2,width=8,bg='light blue',command=lambda:click(5))
btn6=Button(window,text="6",height=2,width=8,bg='light blue',command=lambda:click(6))
btns=Button(window,text="-",height=2,width=8,bg='light blue',command=sub)


btn1=Button(window,text="1",height=2,width=8,bg='light blue',command=lambda:click(1))
btn2=Button(window,text="2",height=2,width=8,bg='light blue',command=lambda:click(2))
btn3=Button(window,text="3",height=2,width=8,bg='light blue',command=lambda:click(3))
btna=Button(window,text="+",height=2,width=8,bg='light blue',command=add)


btn00=Button(window,text="00",height=2,width=8,bg='light blue',command=lambda:click(00))
btn0=Button(window,text="0",height=2,width=8,bg='light blue',command=lambda:click(0))
btnq=Button(window,text=".",height=2,width=8,bg='light blue',command=lambda:click('.'))
btne=Button(window,text="=",height=2,width=8,bg='light blue',command=equal)


btnc.grid(column=0, row=1)
btnM.grid(column=1, row=1)
btndd.grid(column=2, row=1)
btnd.grid(column=3, row=1)

btn7.grid(column=0, row=2)
btn8.grid(column=1, row=2)
btn9.grid(column=2, row=2)
btnm.grid(column=3, row=2)

btn4.grid(column=0, row=3)
btn5.grid(column=1, row=3)
btn6.grid(column=2, row=3)
btns.grid(column=3, row=3)

btn1.grid(column=0, row=4)
btn2.grid(column=1, row=4)
btn3.grid(column=2, row=4)
btna.grid(column=3, row=4)

btn00.grid(column=0, row=5)
btn0.grid(column=1, row=5)
btnq.grid(column=2, row=5)
btne.grid(column=3, row=5)

window=mainloop()