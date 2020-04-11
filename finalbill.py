from tkinter import *
import pyodbc as pd
import record

nameEnt = None
contEnt = None
total = None
bill = None

conn = pd.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-I8FD6VJC\SQL2016;"
    "Database=Restaurant;"
    "Trusted_Connection=yes;"
)


def dis(fitems):
    dispbill(fitems)


def details(event):
    global total
    global nameEnt
    global contEnt
    global bill
    n = nameEnt.get()
    c = contEnt.get()
    record.get(n, c, total)
    bill.destroy()


def dispbill(fitems):
    global nameEnt
    global contEnt
    global total
    global bill

    bill = Tk()
    bill.geometry("300x300")

    cursor = conn.cursor()
    price = []
    f = []
    k = 5
    for i in fitems:
        cursor.execute('select "Food Item","Price" from dbo.Sheet1$ where ID = ' + i)
        for row in cursor.fetchall():
            f.append(row[0])
            price.append(row[1])
        total = sum(price)
        print(total)
        print(f)
    name = Label(bill, text="Name")
    name.grid(row=0, column=0)
    cont = Label(bill, text="Contact No.")
    cont.grid(row=1, column=0)
    nameEnt = Entry(bill)
    nameEnt.grid(row=0, column=1)
    contEnt = Entry(bill)
    contEnt.grid(row=1, column=1)
    for j, l in zip(f, price):
        fitem = Label(bill, text=j)
        fitem.grid(row=k, column=0)
        pr = Label(bill, text=l)
        pr.grid(row=k, column=1)
        k += 1
    Total = Label(bill, text="Total")
    Total.grid(row=19, column=0)
    amt = Label(bill, text=total)
    amt.grid(row=19, column=1)
    finish = Button(bill, text="Finish")
    finish.grid(row=22, column=1)

    finish.bind("<Button-1>", details)
    bill.mainloop()
