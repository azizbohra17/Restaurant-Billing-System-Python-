import pyodbc as pd
from tkinter import *
from tkinter import messagebox


import displaymenu as dp

def get(u, p):
    read(conn, u, p)


def read(conn, u, p):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("select password from dbo.loginfo where Username = '" + u + "'")
    for row in cursor.fetchall():
        if row[0].strip() == p:
            messagebox.showinfo("Validation", "Login Successfull")
            dp.gett()

        else:
            messagebox.showerror("Error", "Wrong Password")


conn = pd.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-I8FD6VJC\SQL2016;"
    "Database=Restaurant;"
    "Trusted_Connection=yes;"
)
