from tkinter import *

from tkinter import messagebox
root = Tk()

root.title('Message Box')

def popup():
    messagebox.showinfo("This is my Popup", "Hello World!")

Button(root, text = "Popup", command= popup).pack()

mainloop()