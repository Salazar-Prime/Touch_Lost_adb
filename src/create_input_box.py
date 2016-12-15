from Tkinter import *
import handle_parameter


def create_entry(title, description, master, index):
    """create a text box for taking parameters from user"""
    box = Toplevel(master)
    box.title(title)
    frame = Frame(box, height=100)
    frame.pack()
    descrip_label = Label(frame, text=description)
    descrip_label.pack(side=TOP)
    value = Text(frame, height=1, width=40)
    value.pack(fill=None)
    bt = Button(frame, text="OK", command=lambda: get_value(box, value, index))
    bt.pack(side=BOTTOM)


def get_value(box, value, index):
    val = value.get("1.0", 'end-1c')
    if not val[len(val)-1] == "\n":
        val = val + "\n"
    handle_parameter.update_line(index, val)
    box.destroy()
