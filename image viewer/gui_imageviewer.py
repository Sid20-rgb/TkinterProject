from tkinter import *
from PIL import ImageTk, Image
root = Tk()

root.iconbitmap("C:/Users/asus/Downloads/icon.ico")
image = Image.open("C:/Users/asus/Downloads/one.png")
image = image.resize((450, 350), Image.ANTIALIAS)
my_image = ImageTk.PhotoImage(image)

image1 = Image.open("C:/Users/asus/Downloads/two.png")
image1 = image1.resize((450, 350), Image.ANTIALIAS)
my_image1 = ImageTk.PhotoImage(image1)

image2 = Image.open("C:/Users/asus/Downloads/three.png")
image2 = image2.resize((450, 350), Image.ANTIALIAS)
my_image2 = ImageTk.PhotoImage(image2)

image3 =Image.open("C:/Users/asus/Downloads/four.png")
image3 = image3.resize((450, 350), Image.ANTIALIAS)
my_image3 = ImageTk.PhotoImage(image3)

image_list = [my_image, my_image1, my_image2, my_image3]

my_label = Label(image = my_image)
my_label.grid(row = 0, column = 0, columnspan = 3)

status = Label(root, text="1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)


def back(image_number):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    button_back.grid(row=1, column=0)
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_forward.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)

    if image_number == 1:
        button_back = Button(root, text = "<<", state = DISABLED)
        button_back.grid(row=1, column=0)
    status = Label(root, text=str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)
def forward(image_number):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number-1])
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    button_back.grid(row=1, column=0)
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_forward.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)
    if image_number == 4:
        button_forward = Button(root, text = ">>", state = DISABLED)
        button_forward.grid(row=1, column=2)
    status = Label(root, text=str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back = Button(root, text= "<<", command = lambda:back(), state = DISABLED)
button_back.grid(row = 1, column = 0)

button_exit = Button(root, text = "EXIT", command = root.quit)
button_exit.grid(row = 1, column = 1)

button_forward = Button(root, text = ">>", command = lambda:forward(2))
button_forward.grid(row = 1, column= 2)

root.mainloop()