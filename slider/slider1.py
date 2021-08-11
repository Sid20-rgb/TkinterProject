from tkinter import *

root = Tk()

vertical = Scale(root, from_=0, to=500)
vertical.pack()

horizontal = Scale(root, from_= 0, to= 500, orient = HORIZONTAL)
horizontal.pack()

def slide():

    my_label = Label(root, text = horizontal.get() + "x" + vertical.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

my_button = Button(root, text = "Click", command = slide).pack()

root.mainloop() #ends