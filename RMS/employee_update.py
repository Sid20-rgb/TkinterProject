from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.geometry("1191x670")

#Define image as background
bg =ImageTk.PhotoImage(file = "add_emp.png")
bg_label = Label(root, image = bg)
bg_label.place(x = 0, y = 0)

#creating labels
name_label = Label(root, text = "Employee Name", bg = "#FFFFFF")
name_label.configure(font = "-family {Poppins} -size 12")
name_label.place(x = 160, y = 185)

contact_label = Label(root, text = "Contact No.", bg = "#FFFFFF")
contact_label.configure(font = "-family {Poppins} -size 12")
contact_label.place(x = 160, y = 265)

citizen_label = Label(root, text = "Citizenship No.", bg = "#FFFFFF")
citizen_label.configure(font = "-family {Poppins} -size 12")
citizen_label.place(x = 160, y = 338)

designation_label = Label(root, text = "Designation", bg = "#FFFFFF")
designation_label.configure(font = "-family {Poppins} -size 12")
designation_label.place(x = 625, y = 185)

address_label = Label(root, text = "Address", bg = "#FFFFFF")
address_label.configure(font = "-family {Poppins} -size 12")
address_label.place(x = 625, y = 265)

password_label = Label(root, text = "Password", bg = "#FFFFFF")
password_label.configure(font = "-family {Poppins} -size 12")
password_label.place(x = 625, y = 338)



#creating buttons
update_bt = Button(root, text = "UPDATE", bg = "#007884", fg= "Black",
                  activebackground="#007884", borderwidth = 0, pady = 0)
update_bt.configure(font = "-family {Poppins} -size 14")
update_bt.place(x = 474, y = 523)

clear_bt = Button(root, text = "Clear", bg = "#007884", fg= "Black",
                  activebackground="#007884", borderwidth = 0)
clear_bt.configure(font = "-family {Poppins} -size 14")
clear_bt.place(x = 655, y = 522)

'''
#creating entryboxes
entry_font = ('Poppins', 12)
searchbox = Entry(root, borderwidth = 0, bg = "#f2f2f2", font = entry_font )
searchbox.place(x = 90, y = 185)'''


root.mainloop()