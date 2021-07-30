from tkinter import *

root = Tk()

root.title("GUI")
e1 = Entry(root, borderwidth = 10, fg = "Green")
e1.pack()

def onClick():
    texte = e1.get()
    display = Label(root, text = texte)
    display.pack()
    button = Button(root, text = texte)
    button.pack()

button1 = Button(root, text = "Submit", command = onClick)
button1.pack()

root.mainloop()