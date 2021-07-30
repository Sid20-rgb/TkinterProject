from tkinter import *

root = Tk()

name = Label(root, text = "Name")
name.grid(row = 0, column = 0)
e1 = Entry(root)
e1.grid(row = 0, column = 1)

password = Label(root, text = "Password")
password.grid(row = 1, column =0)
e2 = Entry(root)
e2.grid(row = 1, column = 1)

submit = Button(root, text = "Submit")
submit.grid(row = 4, column = 1)

root.mainloop()
