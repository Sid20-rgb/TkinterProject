from tkinter import *

root = Tk()

button1 = Button(root, text = "Click")
button1.pack()

button2 = Button(root, text = "Click", state = DISABLED)
button2.pack()

button3 = Button(root, text= "Click", padx = 50, pady = 50)
button3.pack()

root.mainloop()
