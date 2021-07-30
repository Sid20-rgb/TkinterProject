from tkinter import *

root = Tk()

name = Label(root, text = "Name")
name.place(x = 40, y = 120)
address = Label(root, text = "Address")
address.place(x = 40, y = 150)
contact = Label(root, text = "Contact")
contact.place(x = 40, y = 170)

e1 = Entry(root)
e1.place(x = 100, y = 120)
e2 = Entry(root)
e2.place(x = 100, y = 150)
e3 = Entry(root)
e3.place(x = 100, y = 170)

root.mainloop()
