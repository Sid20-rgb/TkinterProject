from tkinter import *

from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()

root.title('Message Box')

# def popup():
#     messagebox.showinfo("This is my Popup", "Hello World!")
#
# Button(root, text = "Popup", command= popup).pack()

# def popup():
#     response = messagebox.askyesno("This is my Popup", "is it pooped up?")
#     if response == 1:
#         Label(root, text = "It is pooped up.").pack()
#     else:
#         Label(root, text = "It is pooped up but clicked NO.").pack()
#
# Button(root, text = "Popup", command = popup).pack()


def popup():
    response = messagebox.showwarning("This is my Popup", "i am afraid it is not pooped up")

Button(root, text = "Popup", command = popup).pack()

root.mainloop()