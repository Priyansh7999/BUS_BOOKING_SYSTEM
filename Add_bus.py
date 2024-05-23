from tkinter import *
from tkcalendar import DateEntry
root=Tk()
root.title("booking")
root.geometry("1000x1000")
img=PhotoImage(file = "starbus.png")
Label(root, image = img).pack()
Label(root,text='Online Bus Booking System',fg='red',bg="light blue",font='Calibri 20').pack()
Button(root,text="New Operator",bg="green",relief='raised',font='times 20').place(x=340,y=350)
Button(root,text="New Bus",bg="green",relief='raised',font='times 20').place(x=540,y=350)
Button(root,text="New Route",bg="green",relief='raised',font='times 20').place(x=690,y=350)
Button(root,text="New Run",bg="green",relief='raised',font='times 20').place(x=870,y=350)
Button(root,text="HOME",bg="green",font='times 12').place(x=1020,y=360)
root.mainloop()