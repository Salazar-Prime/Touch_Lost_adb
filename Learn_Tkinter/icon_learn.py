# learn to add icons
from Tkinter import *
from PIL import Image, ImageTk

root = Tk()

image = Image.open("info.png")
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.pack()

root.mainloop()
