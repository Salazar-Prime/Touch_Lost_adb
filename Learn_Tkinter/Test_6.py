# Arranging everything in classes
from Tkinter import *

class simpleone:

    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.printbt = Button(frame, text="Print Message", command=self.printing)
        self.printbt.pack(side=LEFT)

        self.quitbt = Button(frame, text="Quit", command=frame.quit)
        self.quitbt.pack(side=RIGHT)

    def printing(self):
        print "Working"

root = Tk()
obj = simpleone(root)
root.mainloop()