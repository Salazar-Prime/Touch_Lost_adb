# Function binding

from Tkinter import *

root = Tk()

# frist option
def printname():
    print("My name is varun")

b1 = Button(root, text="print", command=printname)
b1.pack()


# second option
def printname2(event):
    print("My name is varun2")

b2 = Button(root, text="print2")
b2.bind("<Button-3>", printname2)
b2.pack()


root.mainloop()