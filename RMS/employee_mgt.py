from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.geometry("1191x670")

def add_emp():
    global bg
    top = Toplevel()  # using top to call instead of Tk()
    top.title("Add Employee")
    top.geometry("1191x670")
    # Define image as background
    bg = ImageTk.PhotoImage(file="add_emp.png")
    bg_label = Label(top, image=bg)
    bg_label.place(x=0, y=0)

    # creating labels
    name_label = Label(top, text="Employee Name", bg="#FFFFFF")
    name_label.configure(font="-family {Poppins} -size 12")
    name_label.place(x=160, y=185)

    contact_label = Label(top, text="Contact No.", bg="#FFFFFF")
    contact_label.configure(font="-family {Poppins} -size 12")
    contact_label.place(x=160, y=265)

    citizen_label = Label(top, text="Citizenship No.", bg="#FFFFFF")
    citizen_label.configure(font="-family {Poppins} -size 12")
    citizen_label.place(x=160, y=338)

    designation_label = Label(top, text="Designation", bg="#FFFFFF")
    designation_label.configure(font="-family {Poppins} -size 12")
    designation_label.place(x=625, y=185)

    address_label = Label(top, text="Address", bg="#FFFFFF")
    address_label.configure(font="-family {Poppins} -size 12")
    address_label.place(x=625, y=265)

    password_label = Label(top, text="Password", bg="#FFFFFF")
    password_label.configure(font="-family {Poppins} -size 12")
    password_label.place(x=625, y=338)

    # creating entry boxes
    entry_font = ('Poppins', 12)
    namebox = Entry(top, borderwidth=0, font=entry_font)
    namebox.place(x=165, y=220)

    entry_font = ('Poppins', 12)
    contactbox = Entry(top, borderwidth=0, font=entry_font)
    contactbox.place(x=165, y=295)

    entry_font = ('Poppins', 12)
    citizenbox = Entry(top, borderwidth=0, font=entry_font)
    citizenbox.place(x=165, y=368)

    entry_font = ('Poppins', 12)
    designationbox = Entry(top, borderwidth=0, font=entry_font)
    designationbox.place(x=630, y=220)

    entry_font = ('Poppins', 12)
    addressbox = Entry(top, borderwidth=0, font=entry_font)
    addressbox.place(x=630, y=295)

    entry_font = ('Poppins', 12)
    passwordbox = Entry(top, borderwidth=0, font=entry_font)
    passwordbox.place(x=630, y=368)

    # creating buttons
    add_bt = Button(top, text="ADD", bg="#007884", fg="Black",
                    activebackground="#007884", borderwidth=0)
    add_bt.configure(font="-family {Poppins} -size 14")
    add_bt.place(x=490, y=522)

    clear_bt = Button(top, text="Clear", bg="#007884", fg="Black",
                      activebackground="#007884", borderwidth=0)
    clear_bt.configure(font="-family {Poppins} -size 14")
    clear_bt.place(x=655, y=522)

def update_emp():
    global bgg
    root.title("Update Empoloyee")
    # Define image as background
    bgg = ImageTk.PhotoImage(file="update_emp.png")
    bg_label = Label(root, image=bgg)
    bg_label.place(x=0, y=0)

    # creating labels
    name_label = Label(root, text="Employee Name", bg="#FFFFFF")
    name_label.configure(font="-family {Poppins} -size 12")
    name_label.place(x=160, y=185)

    contact_label = Label(root, text="Contact No.", bg="#FFFFFF")
    contact_label.configure(font="-family {Poppins} -size 12")
    contact_label.place(x=160, y=265)

    citizen_label = Label(root, text="Citizenship No.", bg="#FFFFFF")
    citizen_label.configure(font="-family {Poppins} -size 12")
    citizen_label.place(x=160, y=338)

    designation_label = Label(root, text="Designation", bg="#FFFFFF")
    designation_label.configure(font="-family {Poppins} -size 12")
    designation_label.place(x=625, y=185)

    address_label = Label(root, text="Address", bg="#FFFFFF")
    address_label.configure(font="-family {Poppins} -size 12")
    address_label.place(x=625, y=265)

    password_label = Label(root, text="Password", bg="#FFFFFF")
    password_label.configure(font="-family {Poppins} -size 12")
    password_label.place(x=625, y=338)

    # creating entryboxes
    entry_font = ('Poppins', 12)
    namebox = Entry(root, borderwidth=0, font=entry_font)
    namebox.place(x=165, y=220)

    entry_font = ('Poppins', 12)
    contactbox = Entry(root, borderwidth=0, font=entry_font)
    contactbox.place(x=165, y=295)

    entry_font = ('Poppins', 12)
    citizenbox = Entry(root, borderwidth=0, font=entry_font)
    citizenbox.place(x=165, y=368)

    entry_font = ('Poppins', 12)
    designationbox = Entry(root, borderwidth=0, font=entry_font)
    designationbox.place(x=630, y=220)

    entry_font = ('Poppins', 12)
    addressbox = Entry(root, borderwidth=0, font=entry_font)
    addressbox.place(x=630, y=295)

    entry_font = ('Poppins', 12)
    passwordbox = Entry(root, borderwidth=0, font=entry_font)
    passwordbox.place(x=630, y=368)

    # creating buttons
    update_bt = Button(root, text="UPDATE", bg="#007884", fg="Black",
                       activebackground="#007884", borderwidth=0, pady=0)
    update_bt.configure(font="-family {Poppins} -size 14")
    update_bt.place(x=474, y=523)

    clear_bt = Button(root, text="Clear", bg="#007884", fg="Black",
                      activebackground="#007884", borderwidth=0)
    clear_bt.configure(font="-family {Poppins} -size 14")
    clear_bt.place(x=655, y=522)


#Define image as background
bg1 =ImageTk.PhotoImage(file = "Employee_mgt.png")
bg_label = Label(root, image = bg1)
bg_label.place(x = 0, y = 0)

#creating texts
menu_label = Label(root, text = "Menu", bg = "#F2F2F2")
menu_label.configure(font = "-family {Poppins} -size 12")
menu_label.place(x = 135, y = 85)

id_label = Label(root, text = "Employee ID", bg = "#F2F2F2")
id_label.configure(font = "-family {Poppins} -size 12")
id_label.place(x = 90, y = 128)

options_label = Label(root, text = "Employee Options", bg = "#F2F2F2")
options_label.configure(font = "-family {Poppins} -size 12")
options_label.place(x = 90, y = 220)

#creating buttons
login_bt = Button(root, text = "Log Out", bg = "#007884", activebackground="#007884", borderwidth = 0)
login_bt.configure(font = "-family {Poppins} -size 14")
login_bt.place(x = 1046, y = 607)

search_bt = Button(root, text = "Search", bg = "#007884", activebackground = "#007884", borderwidth = 0)
search_bt.configure(font = "-family {Poppins} -size 14")
search_bt.place(x = 315, y = 138)

add_bt = Button(root, text = "ADD Employee", bg = "#007884", activebackground = "#007884", borderwidth = 0,
                command = add_emp)
add_bt.configure(font = "-family {Poppins} -size 14")
add_bt.place(x = 156, y = 280)

update_bt = Button(root, text = "UPDATE Employee", bg = "#007884", activebackground = "#007884", borderwidth = 0,
                   command = update_emp)
update_bt.configure(font = "-family {Poppins} -size 14")
update_bt.place(x = 140, y = 360)

delete_bt = Button(root, text = "DELETE Employee", bg = "#007884", activebackground = "#007884", borderwidth = 0)
delete_bt.configure(font = "-family {Poppins} -size 14")
delete_bt.place(x = 140, y = 440)

exit_bt = Button(root, text = "EXIT", bg = "#007884", activebackground = "#007884", borderwidth = 0)
exit_bt.configure(font = "-family {Poppins} -size 14")
exit_bt.place(x = 200, y = 540)

#creating entry box
entry_font = ('Poppins', 12)
searchbox = Entry(root, borderwidth = 0, bg = "#f2f2f2", font = entry_font )
searchbox.place(x = 105, y = 160)


root.mainloop()