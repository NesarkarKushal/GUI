import thingspeak.cmdline
from tkinter import  *

channel=thingspeak.Channel(Enter_ID of ThinkSpeak Cloud,api_key="Enter_Key from Thinkspeak Cloud",fmt='txt')

root=Tk()
root.geometry("400x400")
root.title("EdGate Technologies - Things Speak Cloud")
root.configure(bg="Gray")


def Write():
    data=txt.get()
    channel.update({'field1':data})
    txt.delete(0,END)


def Read():
    data=channel.get_field_last(field=1)
    # print(data)
    txt1.delete(0,END)
    txt1.insert(0,str(data))

txt=Entry(root,font=("timsnewroman Bold",14))
txt.place(bordermode='outside',x=20,y=20,width=355,height=30)

Btn=Button(root,text="Write",command=Write)
Btn.place(x=180,y=55)

txt1=Entry(root,font=("timsnewroman Bold",14))
txt1.place(bordermode='outside',x=20,y=90,width=355,height=30)

Btn1=Button(root,text="Read",command=Read)
Btn1.place(x=180,y=130)

root.mainloop()