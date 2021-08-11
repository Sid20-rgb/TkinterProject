from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.geometry("1191x670")



#Define image as background
bg =ImageTk.PhotoImage(file = "back.png")
bg_label = Label(root, image = bg)
bg_label.place(x = 0, y = 0)


#adding admin icon and text at the top
img_ad = Image.open("C:/Users/asus/Pictures/Saved Pictures/admin.png")
resized_ad = img_ad.resize((40, 30), Image.ANTIALIAS)
img_ad = ImageTk.PhotoImage(resized_ad)
img_label = Label(root, image = img_ad, bg = "White", fg= "Black")
img_label.place(x = 5, y = 0)

#admin label text
admin_label = Label(root, text = "ADMIN", bg = "Black", fg = "White")
admin_label.configure(font = "-family {Poppins} -size 12")
admin_label.place(x = 5, y = 20)

#Creating inventory button and adding image in inventory button
img_inv = Image.open("C:/Users/asus/Pictures/Saved Pictures/inventory.png")
resized_inv = img_inv.resize((40, 30), Image.ANTIALIAS )
img_inv = ImageTk.PhotoImage(resized_inv)
bt_inv = Button(root, text = "Inventory", padx = 25, pady = 27, image = img_inv, compound = TOP)
bt_inv.configure(font="-family {Poppins} -size 12", relief  ="flat", overrelief = "flat", activebackground = "#ffffff",
                 cursor = "hand2",
                 borderwidth = "0",
                 foreground = "#333333",
                 background = "#ffffff")
bt_inv.place(x = 550, y = 250)

#Creating Employees button
img_emp = Image.open("C:/Users/asus/Pictures/Saved Pictures/employees.png")
resized_emp = img_emp.resize((40, 30), Image.ANTIALIAS )
img_emp = ImageTk.PhotoImage(resized_emp)
bt_emp = Button(root, text = "Employees", padx = 25, pady = 27, image = img_emp, compound = TOP)
bt_emp.configure(font="-family {Poppins} -size 12", relief  ="flat", overrelief = "flat", activebackground = "#ffffff",
                 cursor = "hand2",
                 borderwidth = "0",
                 foreground = "#333333",
                 background = "#ffffff")

bt_emp.place(x = 800, y = 250)
'''
img_invo = Image.open("C:/Users/asus/Pictures/Saved Pictures/invoices.png")
resized_invo = img_invo.resize((50, 30), Image.ANTIALIAS )
img_invo = ImageTk.PhotoImage(resized_inv)
bt_invo = Button(root, text = "Invoices", padx = 35, pady = 27, image = img_inv, compound = TOP)
bt_invo.configure(font="-family {Poppins} -size 12", relief  ="flat", overrelief = "flat", activebackground = "#ffffff",
                 cursor = "hand2",
                 borderwidth = "0",
                 foreground = "#333333",
                 background = "#ffffff")
bt_inv.place(x = 550, y = 450)'''

img_invo = PhotoImage(file = "invbut.png")
invo_label = Label(image = img_invo)
invo_label.place(x = 550, y = 450)
bt_invo = Button(root, image = img_invo)


root.mainloop()



