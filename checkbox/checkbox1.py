from tkinter import *

root = Tk()

def show():
    my_label = Label(root, text = var.get()).pack()

var = StringVar()

checkbutton = Checkbutton(root, text = "Tick", variable = var, onvalue = "Ticked", offvalue = "Unticked")
checkbutton.deselect()
checkbutton.pack()

my_button = Button(root, text = "Show Selection", command = show).pack()

root.mainloop()

