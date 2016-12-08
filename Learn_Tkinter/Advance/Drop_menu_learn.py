# Learning to make drop down menu
from Tkinter import *

def doNothing():
    print "doing nothing"

root = Tk()

drop_menu = Menu(root)
root.config(menu=drop_menu)

submenu = Menu(drop_menu)
drop_menu.add_cascade(label="file", menu=submenu)
submenu.add_command(label="New project...", command=doNothing)
submenu.add_command(label="New...", command=doNothing)
submenu.add_separator()
submenu.add_command(label="Exit", command=root.quit)

editmenu = Menu(drop_menu)
drop_menu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Paste", command=doNothing)

root.mainloop()