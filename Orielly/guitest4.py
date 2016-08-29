from Tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")



root.mainloop()