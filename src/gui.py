"""Setting up the GUI"""

from Tkinter import *
from PIL import Image, ImageTk


class GUI:

    def printing(self):
        self.status_bar.config(text="BYE")
        print "Working"

    def __init__(self, master):

        # setting up icons for UI
        image = Image.open("resources/exit.png")
        self.quit_icon = ImageTk.PhotoImage(image)
        image = Image.open("resources/about.png")
        self.about_icon = ImageTk.PhotoImage(image)
        image = Image.open("resources/help.png")
        self.help_icon = ImageTk.PhotoImage(image)
        image = Image.open("resources/sync.png")
        self.rstadb_icon = ImageTk.PhotoImage(image)
        image = Image.open("resources/diagram.png")
        self.rlddev_icon = ImageTk.PhotoImage(image)
        image = Image.open("resources/app.png")
        self.pathadb_icon = ImageTk.PhotoImage(image)

        # adding toolbar
        toolbar = Frame(master)
        toolbar.pack(fill=X)

        self.rstadb = Button(toolbar, text="Restart ADB", image=self.rstadb_icon, compound=TOP, command=self.printing)
        self.rstadb.pack(side=LEFT)

        self.rlddev = Button(toolbar, text="Reload Devices", image=self.rlddev_icon, compound=TOP)
        self.rlddev.pack(side=LEFT)

        self.help = Button(toolbar, text="    Help    ", image=self.help_icon, compound=TOP)
        self.help.pack(side=LEFT)

        self.about = Button(toolbar, text="    About    ", image=self.about_icon, compound=TOP)
        self.about.pack(side=LEFT)

        self.quit = Button(toolbar, text="    Quit    ", image=self.quit_icon, compound=TOP, command=master.quit)
        self.quit.pack(side=LEFT)

        # adding device list
        dev_list = Frame(master, height=150)
        dev_list.pack(fill=X)

        # adding status bar
        self.status_bar = Label(master, text="Welcome", bd=1, relief=SUNKEN, anchor=W)
        self.status_bar.pack(side=BOTTOM, fill=X)

        # adding menu bar
        menu_bar = Menu(master)
        master.config(menu=menu_bar)

        self.sub_file = Menu(menu_bar)
        menu_bar.add_cascade(label="File", menu=self.sub_file)
        self.sub_file.add_command(label="  Exit", image=self.quit_icon, compound=LEFT, command=master.quit)

        self.sub_ADB = Menu(menu_bar)
        menu_bar.add_cascade(label="ADB", menu=self.sub_ADB)
        self.sub_ADB.add_command(label="  Set ADB path", image=self.pathadb_icon, compound=LEFT)
        self.sub_ADB.add_command(label="  Restart ADB", image=self.rstadb_icon, compound=LEFT)
        self.sub_ADB.add_command(label="  Reload Devices", image=self.rlddev_icon, compound=LEFT)

        self.sub_help = Menu(menu_bar)
        menu_bar.add_cascade(label="Help", menu=self.sub_help)
        self.sub_help.add_command(label="  Help", image=self.help_icon, compound=LEFT)
        self.sub_help.add_command(label="  About", image=self.about_icon, compound=LEFT)

# root = Tk()
# obj = GUI(root)
# root.mainloop()