from tkinter import *

root = Tk()

frame = LabelFrame(root, text = "My frame", padx = 30, pady = 30)
frame.pack(padx= 10, pady = 10)
e = Entry(frame)
e.pack()

def onClick():
    e_g = e.get()
    display = Label(frame, text = e_g)
    display.pack()
button = Button(frame, text = "CLICK", command = onClick)
button.pack()

root.mainloop()