from tkinter import *
from tkinter.messagebox import *
import sqlite3
from time import strftime
con = sqlite3.Connection("my_datbase")
cur = con.cursor()
root=Tk()
cur.execute("select date()")
string=strftime('%H:%M%S')
root.config(text=string)

Label(root,text=cur.fetchall(),font='times 11 bold').pack()
con.commit()
root.mainloop()