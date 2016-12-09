# Learning to update text in status bar and adding icon to button

from Tkinter import *
from PIL import Image, ImageTk

root = Tk()
i = 0
def update_label():
    global i
    status.config(text=i)
    i += 1


# adding status bar
status = Label(root, text="v", bd=1, relief=SUNKEN, anchor = W)
status.pack(side=BOTTOM, fill = X)

# adding icon button
image = Image.open("info.png")
photo = ImageTk.PhotoImage(image)
b = Button(root, command=update_label, text="UPDATE", image=photo, compound=TOP)
b.pack(side=TOP)

root.mainloop()


