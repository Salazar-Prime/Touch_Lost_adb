# Learning to make Toolbar

from Tkinter import *

def doNothing():
    print "doing nothing"

root = Tk()

toolbar = Frame(root, bg="blue")
insertbt = Button(toolbar, text="Insert Image", command=doNothing)
insertbt.pack(side=LEFT, padx=2, pady=2)
printbt = Button(toolbar, text="Print Image", command=doNothing)
printbt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)
root.mainloop()