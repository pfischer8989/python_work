from Tkinter import *

class Application(Frame):
    """Application main window class."""
    def __init__(self, master=None):
        """Main frame initialization (mostly delegated)"""
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        """Add all the widgets to the main frame."""
        top_frame = Frame(self)
        self.text_in1 = Entry(top_frame)
        self.text_in2 = Entry(top_frame)
        self.label = Label(top_frame, text="Output")
        self.text_in1.pack(side=LEFT)
        self.text_in2.pack(side=RIGHT)
        self.label.pack()
        self.r = IntVar()
        top_frame.pack(side=TOP)

        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP)
        self.QUIT = Button(bottom_frame, text="Quit", command=self.quit)
        self.QUIT.pack(side=LEFT)
        self.handleb = Button(bottom_frame, text="Sum", command=self.handle)
        self.handleb.pack(side=LEFT)

    def handle(self):
        """Handle a click of the button by processing any text the
        user has placed in the Entry widget according to the selected
        radio button."""
        text1 = self.text_in1.get()
        text2 = self.text_in2.get()

        
        try:
            f1 = float(text1)
            f2 = float(text2)

            output = f1 + f2
        except:
            output = "****ERROR****"   

        self.label.config(text=output)
            
root = Tk()
app = Application(master=root)
app.mainloop()
