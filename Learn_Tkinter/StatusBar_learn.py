# Learning to make Status Bar

from Tkinter import *

root = Tk()

def doNothing():
    print "doing nothing"

status = Label(root, text="Preparing to do nothing", bd=1, relief=SUNKEN, anchor = W)
status.pack(side=BOTTOM, fill = X)


root.mainloop()