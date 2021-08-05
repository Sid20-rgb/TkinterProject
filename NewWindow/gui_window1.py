from tkinter import *
from PIL import ImageTk, Image

root = Tk()

def popup():
    top = Toplevel() #using top to call instead of Tk()
    top.title("New Window")
    my_image = Image.open("C:/Users/asus/Desktop/one.png")
    my_image = my_image.resize((450, 350), Image.ANTIALIAS)
    f_image = ImageTk.PhotoImage(my_image)
    display = Label(top, image = f_image)
    display.pack()
    close = Button(top, text = "Close", command = root.destroy).pack()

Button(root, text = "Open", command = popup).pack()
root.mainloop()