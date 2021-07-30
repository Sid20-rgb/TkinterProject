from tkinter import *

from PIL import ImageTk, Image

root = Tk()

my_image = ImageTk.PhotoImage(Image.open("C:/Users/asus/desktop/ff.png"))
my_label = Label(imaeg= my_image)
my_label.pack()

button = Button(root, text = "Exit", command = root.quit, width = 20)
button.pack()

root.mainloop()