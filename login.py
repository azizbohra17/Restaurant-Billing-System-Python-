from tkinter import *
import verification as ver


def sub(event):
    u = userEnt.get()
    p = passwordEnt.get()
    ver.get(u, p)
    login.destroy()


login = Tk()
login.title("Login")
login.geometry("400x200")
user = Label(login, text="Username").place(x=30, y=50)
password = Label(login, text="Password").place(x=30, y=90)
sb = Button(login, text="Submit")
sb.place(x=30, y=130)

userEnt = Entry(login)
userEnt.place(x=100, y=50)
passwordEnt = Entry(login, show="*")
passwordEnt.place(x=100, y=90)

sb.bind("<Button-1>", sub)
login.mainloop()
