# learn to draw shapes in canvas

from Tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

blackline = canvas.create_line(0, 0, 200, 50)
redline = canvas.create_line(0, 100, 200, 50, fill="red")
greenbox = canvas.create_rectangle(25, 25, 130, 60, fill="green")

canvas.delete(redline)
# delete all graphics from screen
# canvas.delete(ALL)

root.mainloop()