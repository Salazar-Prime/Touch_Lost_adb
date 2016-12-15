from Tkinter import *
import src.constants, src.gui
from src.create_input_box import create_entry


root = Tk()

# assigning constants from file
from src.handle_parameter import read_line
for i in range(len(src.constants.param_consts)):
    src.constants.param_consts[i] = read_line(i)
del read_line

# checking if anyone of the parameters is null
for i in range(len(src.constants.param_consts)):
    if src.constants.param_consts[i] == None:
        if i == 0:
            create_entry("ADB_path", "Enter directory which contains adb.exe", root, i)
        elif i == 1:
            create_entry("device_img", "wow", root, i)
        elif i == 2:
            create_entry("host_img", "wow", root, i)

# setting up GUI
obj = src.gui.GUI(root)
root.mainloop()
