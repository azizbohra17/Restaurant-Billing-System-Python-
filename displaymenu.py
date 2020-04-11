from tkinter import *
import pyodbc as pd
import finalbill

fitems = []
it = None
display = None
wind = None

def add(event):
    global it
    item = it.get()
    #item = int(item)
    fitems.append(item)
    print(fitems)

def final(event):
    finalbill.dispbill(fitems)
    display.destroy()
    wind.destroy()

def gett():
    disp(conn)


def disp(conn):
    global display
    display = Tk()
    cursor = conn.cursor()
    cursor.execute('SELECT "ID","Food Item" FROM dbo.Sheet1$')
    food = []
    for row in cursor:
        row[0] = int(row[0])
        food.append(row)
    print(food)
    i = 0
    k = 0
    for j in range(50):
        if i < 25:
            item = Label(display, text=food[i])
            item.grid(row=j, column=0)
        elif i > 25:
            item = Label(display, text=food[i])
            item.grid(row=k, column=1)
            k += 1
        i += 1
    getItem(food)
    display.mainloop()


def getItem(food):
    global wind
    global it
    wind = Tk()
    wind.geometry("300x200")
    item = Label(wind, text="Enter Item No.")
    item.place(x=20, y=60)
    it = Entry(wind)
    it.place(x=120, y=60)
    add1 = Button(wind, text="Add")
    add1.place(x=50, y=100)
    final1 = Button(wind, text="Final Bill")
    final1.place(x=100, y=100)

    add1.bind("<Button-1>", add)
    final1.bind("<Button-1>", final)
    wind.mainloop()


conn = pd.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-I8FD6VJC\SQL2016;"
    "Database=Restaurant;"
    "Trusted_Connection=yes;"
)
# disp(conn)

