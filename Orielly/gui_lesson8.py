from Tkinter import *

ALL = N+S+W+E

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()


       
        for r in range(6):
            self.master.rowconfigure(r, weight=1)
          
       
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            Button(master, text="Button {0}".format(c)).grid(row=6, column=c, sticky=ALL)

        flabel1 = Label(master, text="Frame 1", fg="red", bg="blue") 
        flabel2 =  Label(master, text="Frame 2", fg="yellow", bg="green")
        flabel3 =  Label(master, text="Frame 3", fg="white", bg="black")

       # f1 = Frame(master, bg="yellow")
        flabel1.grid(row=0, column=0, rowspan=3, columnspan=2, sticky=ALL)
       
       
         
       # f2 = Frame(master, bg="black")
        flabel2.grid(row=3, column=0, rowspan=3, columnspan=2, sticky=ALL)
        
      
       # f3 = Frame(master, bg="white")
        flabel3.grid(row=0, column=2, rowspan=6, columnspan=3, sticky=ALL)
        
       
root = Tk()
app = Application(master=root)                
app.mainloop()