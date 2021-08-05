from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()

root.title("Dialog Box")

def open():

    top = Toplevel()

    root.filename = filedialog.askopenfilename(initialdir = "/Downloads",
                                               title = "Select a file",
                                               filetype = (("png files", "*.png"),
                                                           ("all files", "*.*")))
    my_label = Label(root, text = root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    image_label = Label(root, image = my_image).pack()

my_button = Button(root, text = "Open", command = open).pack()

root.mainloop()



