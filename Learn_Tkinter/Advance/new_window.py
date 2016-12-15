# create new window with tkinter
from Tkinter import *


def new_win(master):
    box = Toplevel(master)
    box.title("cool")
    fr =Frame(box, width=200, height=200)
    fr.pack()

root = Tk()
frame = Frame(root, width=300, height =100)
frame.pack()
bt = Button(frame, text="press me!", command=lambda: new_win(root))
bt.pack()
root.mainloop()
