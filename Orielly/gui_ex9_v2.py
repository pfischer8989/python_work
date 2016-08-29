from Tkinter import *
import glob

ALL = N+S+W+E

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)


       
        for r in range(6):
            self.rowconfigure(r, weight=1)
       

        self.columnconfigure(0, weight=1)
        Button(self, text="Red", command=self.colred).grid(row=6, column=0, sticky=ALL)
        self.columnconfigure(1, weight=1)
        Button(self, text="Blue", command=self.colblue).grid(row=6, column=1, sticky=ALL)
        self.columnconfigure(2, weight=1)
        Button(self, text="Green", command=self.colgreen).grid(row=6, column=2, sticky=ALL)
        self.columnconfigure(3, weight=1)
        Button(self, text="Black", command=self.colblack).grid(row=6, column=3, sticky=ALL)
        self.columnconfigure(4, weight=1)
        Button(self, text="Open", command=self.capture).grid(row=6, column=4, sticky=ALL)


        # Frame Creation
        frame1 = Frame(self, bg="blue")
        frame2 = Frame(self, bg="green")
        frame3 = Frame(self)
       

        #Frame Placement
        frame1.grid(row=0, column=0, rowspan=3, columnspan=2, sticky=ALL)    
        frame2.grid(row=3, column=0, rowspan=3, columnspan=2, sticky=ALL)
        frame3.grid(row=0, column=2, rowspan=6, columnspan=3, sticky=ALL)     
      

        # Frame Events
        frame1.bind("<Button-1>", self.handler1)
        frame2.bind("<Button-1>", self.handler2)



        # Label Creation
        flabel1 = Label(self, text="Frame 1", fg="red", bg="blue")
        flabel2 = Label(self, text="Frame 2", fg="yellow", bg="green")
       # flabel3 = Label(self, text="Frame 3", fg="white", bg="black")

        # Label Placement
        flabel1.grid(row=0, column=0, rowspan=3, columnspan=2, sticky=W+E)
        flabel2.grid(row=3, column=0, rowspan=3, columnspan=2, sticky=W+E)
      

        # Entry Creation 

        entry1 = Entry(frame3)
        # You need to do this to create the actual object instance
        self.entry1 = entry1

        
        
        # Entry Placement
        self.entry1.columnconfigure(5, weight=1)
        entry1.grid(row=0, column=2, rowspan=1, columnspan=3, sticky=ALL)
        

        # Text Creation
        
        text1 = Text(frame3)

        self.text1 = text1


        # Text Placement
        text1.grid(row=1, column=2, rowspan=5, columnspan=3, sticky=ALL)
        self.text1.columnconfigure(0, weight=1)

        


    def handler1(self, event):
        print("Frame 1 clicked at", event.x, event.y)


    def handler2(self, event):
        print("Frame 2 clicked at", event.x, event.y)

    def capture(self):

        boo = self.entry1.get()
        dir = glob.glob("*.*")

        for x in dir:
            if x == boo:
                f = open(x, 'r')
                contents = f.read()
                self.text1.insert(END, contents, 'txtcon')
                f.close()
    
    def colred(self):      
        self.text1.tag_configure('txtcon', foreground='red')
     
    def colblue(self):      
        self.text1.tag_configure('txtcon', foreground='blue')
       

    def colgreen(self):        
        self.text1.tag_configure('txtcon', foreground='green')
      

    def colblack(self):        
        self.text1.tag_configure('txtcon', foreground='black')   
        
       
root = Tk()
app = Application(master=root)                
app.mainloop()