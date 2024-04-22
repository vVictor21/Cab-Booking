from tkinter import *
from tkinter import ttk
import random
import time
from tkinter import messagebox as ms
import sqlite3

with sqlite3.connect('Users.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS User(username TEXT NOT NULL, password TEXT NOT NULL)')
db.commit()
db.close()


class User:
    def __init__(self, master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.widgets()

    def widgets(self):
        self.head = Label(self.master, text="Login Panel", font=("Arial,20"), pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Username', font=("20"), padx=5, pady=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('15')).grid(row=0, column=1)
        Label(self.logf, text='Password', font=("20"), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('15')).grid(row=1, column=1)
        Button(self.logf, text="Login", bd=1, font=('15'), padx=5, pady=5, command=self.login, bg='green').grid()
        Button(self.logf, text="Create Account", bd=1, font=('15'), padx=5, pady=5, command=self.cr, bg='red').grid(
            row=2, collumn=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='Username', font=("20"), padx=5, pady=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('15')).grid(row=0, column=1)
        Label(self.crf, text='Password', font=("20"), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('15')).grid(row=1, column=1)
        Button(self.crf, text="Create Account", bd=1, font=('15'), padx=5, pady=5, command=self.new_user, bg='green').grid()
        Button(self.crf, text="Go to login", bd=1, font=('15'), padx=5, pady=5, command=self.logf, bg='red').grid(
            row=2, collumn=1)




if __name__ == '__main__':
    root = Tk()
    w = 1150
    h = 650
    geometry = '%dx%d+%d+%d' % (w, h, 50, 0)
    root.geometry("500x300+320+200")
    root.title("Login Form")
    application = User(root)
    root.mainloop()
