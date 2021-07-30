from tkinter import *

root = Tk()

frame = LabelFrame(root, text = "My frame", padx = 5, pady = 5)
frame.pack(padx= 10, pady = 10)

button = Button(frame, text = "CLICK")
button.pack()

root.mainloop()