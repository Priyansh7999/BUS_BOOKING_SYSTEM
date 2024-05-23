from tkinter import *
from tkinter.messagebox import *
from tkcalendar import DateEntry
import datetime as dt
import sqlite3
root=Tk()
root.title("booking")
root.geometry("1000x1000")
con = sqlite3.Connection("my_datbase")
cur = con.cursor()
img=PhotoImage(file = "starbus.png")
Label(root, image = img).pack()
Label(root,text='Online Bus Booking System',fg='red',bg="light blue",font='Calibri 30').place(x=450,y=270)
Label(root,text='From ').place(x=340,y=350)
e6=Entry(root)
e6.place(x=380,y=350)
Label(root,text='To ').place(x=520,y=350)
e7=Entry(root)
e7.place(x=570,y=350)
Label(root,text='Date ').place(x=720,y=350)
def get_date():
    selected_date = e8.get()
e8=DateEntry(root, date_pattern="yyyy-mm-dd")
e8.place(x=790,y=350)
def Proceed_To_Book():
    Label(root,text='Fill Passenger Detail To Book The Seat',fg='red',bg="light blue",font='times 15 bold').place(x=460,y=600)
    Label(root,text="Name").place(x=220,y=650)
    e1=Entry(root)
    e1.place(x=260,y=650)
    Label(root,text="Gender").place(x=400,y=650)
    e2=Entry(root)
    e2.place(x=450,y=650)
    Label(root,text="No. Of Seats").place(x=590,y=650)
    e3=Entry(root)
    e3.place(x=660,y=650)
    Label(root,text="Mobile No.").place(x=740,y=650)
    e4=Entry(root)
    e4.place(x=810,y=650)
    Label(root,text="Age").place(x=920,y=650)
    e5=Entry(root)
    e5.place(x=950,y=650)
    def book_seat():
        c=askyesno("fare Confirm",f" YOUR SEAT IS BOOKED")
        if c==True:
            cur.execute("create table if not exists ticket(name varchar(20),gender varchar(10),seats int,mobile_no int,age int,travel_date date,boarding_point varchar(20),final_point varchar(20))")
            cur.execute("insert into ticket values (?,?,?,?,?,?,?,?)",(str(e1.get()),str(e2.get()),int(e3.get()),int(e4.get()),int(e5.get()),str(e8.get_date()),str(e6.get()),str(e7.get())))
            con.commit()
        else:
            pass
    Button(root,text="BOOK",command=book_seat,bg="green",relief='raised',font='times 10 ').place(x=1100,y=650)

x=0
def show_bus():
    Label(root,text="Select Bus",fg="green",font="times 15 bold").place(x=240,y=380)
    Label(root,text="Operator",fg="green",font="times 15 bold").place(x=400,y=380)
    Label(root,text="Bus Type",fg="green",font="times 15 bold").place(x=550,y=380)
    Label(root,text="Capacity",fg="green",font="times 15 bold").place(x=700,y=380)
    Label(root,text="Fare",fg="green",font="times 15 bold").place(x=840,y=380)
    Button(root,text=f"Proceed To Book",command=Proceed_To_Book,bg="green",relief='raised',font='times 10 ').place(x=900,y=420)
    
    cur.execute("select name from emp ")
    items = cur.fetchall() 
    z=420
    i=1
    for item in items:
        Label(root,text=item,font='times 11 bold').place(x=400,y=z)
        Button(root,text=f"Bus {i}",command=show_bus,bg="green",relief='raised',font='times 10 ').place(x=250,y=z)
        i=i+1
        z=z+40 
    con.commit()


    z=420
    cur.execute("select bus_type from bus")
    items2=cur.fetchall() 
    for item in items2:
        Label(root,text=item,font='times 11 bold').place(x=550,y=z)
        z=z+40
    con.commit()
    z=420
    
    cur.execute("select capacity from bus")
    items3=cur.fetchall()
    for item in items3:
        Label(root,text=item,font='times 11 bold').place(x=700,y=z)
        z=z+40
    con.commit()
    z=420
    cur.execute("select fare from bus")
    item4=cur.fetchall()
    for item in item4:
         Label(root,text=item,font='times 11 bold').place(x=840,y=z)
         z=z+40
    con.commit()
    z=420 
    
    
Button(root,text="SHOW",command=show_bus,bg="green",relief='raised',font='times 10').place(x=900,y=350)
Button(root,text="HOME",bg="green",font='times 10').place(x=970,y=350)
root.mainloop()