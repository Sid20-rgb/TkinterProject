from tkinter import *
import sqlite3

root = Tk()

#creating a database
conn = sqlite3.connect("recording_book.db")

#creating cursor
c = conn.cursor()
'''
#creating table
c.execute(""" CREATE TABLE addresses(first_name text,  
                                    last_name, text,
                                    address text
                                    city text,
                                    state text,
                                    zipcode integer
                                    )""")
print("Created a table.")'''

def submit():
    conn = sqlite3.connect("recording_book.db")

    c = conn.cursor()

    c.execute("INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :zipcode)",{
        "first_name": e1.get(),
        "last_name": e2.get(),
        "address": e3.get(),
        "city": e4.get(),
        "state": e5.get(),
        "zipcode": e6.get()
    })

    print("Address in inserted successfully.")

    conn.commit()
    conn.close()

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)


def query():
    conn = sqlite3.connect("recording_book.db")
    
    c = conn.cursor()
    
    c.execute("SELECT *, oid FROM addresses")
    
    record = c.fetchall()
    print(record)
    
    print_record = " "
    for records in record:
        print_record += str(records)+ "\n"
    
    query_label = Label(root, text = print_record)
    query_label.grid(row = 8, column = 0, columnspan = 2)
    
    conn.commit()
    conn.close()

#desigining
first_name = Label(root, text = "First Name")
first_name.grid(row = 0, column = 0)
e1 = Entry(root)
e1.grid(row = 0, column= 1)

last_name = Label(root, text = "Last Name")
last_name.grid(row= 2, column = 0)
e2 = Entry(root)
e2.grid(row = 2, column = 1)

address = Label(root, text = "Address")
address.grid(row = 3, column = 0)
e3 = Entry(root)
e3.grid(row = 3, column = 1)

city = Label(root, text = "City")
city.grid(row = 4, column = 0)
e4 = Entry(root)
e4.grid(row = 4, column = 1)

state = Label(root, text = "State")
state.grid(row = 5, column = 0)
e5 = Entry(root)
e5.grid(row = 5, column = 1)

zipcode = Label(root, text = "Zip Code")
zipcode.grid(row = 6, column = 0)
e6 = Entry(root)
e6.grid(row =6, column = 1 )

button1= Button(root, text = "Submit", command = submit)
button1.grid(row = 7, column = 1)

button2 = Button(root, text = "Show Record")
button2.grid(row = 8, column = 1)

conn.commit()

conn.close()

root.mainloop()
