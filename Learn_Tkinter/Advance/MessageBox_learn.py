# insert a messag box
from Tkinter import *
import tkMessageBox

root = Tk()
tkMessageBox.showinfo('Tilte', 'Message write')
a = tkMessageBox.askquestion('Question', 'What do you want')
print a

root.mainloop()