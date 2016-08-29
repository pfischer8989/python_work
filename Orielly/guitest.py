from Tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title("Grid Manager")

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        for i in range(5):
            self.master.button = Button(master, text = "Button {0}".format(i))
            self.master.button.pack(side=RIGHT)

        self.Frame1 = Frame(master, bg="red")
        self.Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S) 
        self.Frame2 = Frame(master, bg="blue")
        self.Frame2.grid(row = 2, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)
        self.Frame3 = Frame(master, bg="green")
        self.Frame3.grid(row = 0, column = 2, rowspan = 6, columnspan = 3, sticky = W+E+N+S)

root = Tk()
app = Application(master=root)
app.mainloop()