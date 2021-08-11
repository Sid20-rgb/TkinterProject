from tkinter import *

from PIL import ImageTk, Image

root = Tk()

image = Image.open("C:/Users/asus/Downloads/eng.jpg")
image = image.resize((450, 350), Image.ANTIALIAS)
my_image = ImageTk.PhotoImage(image)

image1 = Image.open("c:/Users/asus/Downloads/three.png")
image1 = image1.resize((450, 350), Image.ANTIALIAS)
my_image1 = ImageTk.PhotoImage(image1)

image_list = [my_image, my_image1]
my_label = Label(image= my_image1)
my_label.grid(row = 0,  column= 0)

button = Button(root, text = "Exit", command = root.quit, width = 20)
button.grid(row = 1, column = 0)

root.mainloop()