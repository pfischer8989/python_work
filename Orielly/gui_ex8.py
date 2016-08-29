from tkinter import *

ALL = N+S+W+E

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)


       
        for r in range(6):
            self.rowconfigure(r, weight=1)
          
       
        for c in range(5):
            self.columnconfigure(c, weight=1)
            Button(self, text="Button {0}".format(c)).grid(row=6, column=c, sticky=ALL)

        frame1 = Frame(self, bg="blue")
        frame1.grid(row=0, column=0, rowspan=3, columnspan=2, sticky=ALL)
        frame2 = Frame(self, bg="green")
        frame2.grid(row=3, column=0, rowspan=3, columnspan=2, sticky=ALL)
        frame3 = Frame(self, bg="black")
        frame3.grid(row=0, column=2, rowspan=6, columnspan=3, sticky=ALL)

        flabel1 = Label(self, text="Frame 1", fg="red", bg="blue")
        flabel2 = Label(self, text="Frame 2", fg="yellow", bg="green")
        flabel3 = Label(self, text="Frame 3", fg="white", bg="black")

        flabel1.grid(row=0, column=0, rowspan=3, columnspan=2, sticky=W+E)
          
        flabel2.grid(row=3, column=0, rowspan=3, columnspan=2, sticky=W+E)
        
        flabel3.grid(row=0, column=2, rowspan=6, columnspan=3, sticky=W+E)
        
       
root = Tk()
app = Application(master=root)                
app.mainloop()