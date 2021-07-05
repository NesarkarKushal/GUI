from tkinter import *
from tkinter import Menu

window = Tk()
window.title("EdGate Technologies")
window.geometry("400x400")

menu = Menu(window)

new_item = Menu(menu)
menu.add_cascade(label='File', menu=new_item)
new_item.add_command(label='New file')
new_item.add_command(label='save as')

new_item1 = Menu(menu)
menu.add_cascade(label='Edit', menu=new_item1)
new_item1.add_command(label='cut')
new_item1.add_command(label='paste')
window.config(menu=menu)
window.mainloop()