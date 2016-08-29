
from tkinter import *

class Application(Frame):
    def say_hi(self):
        print("Hi there, everyone!")

    def createWidgets(self):
        self.QUIT = Label(self, text="Goodbye", bg="red", fg="blue")
        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self, text="hello", bg="blue", fg="red", command=self.say_hi)
        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
