from tkinter import *
from tkinter import ttk
import random
import time
from tkinter import messagebox as ms
import sqlite3

class user:
    def __init__(self,master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.widgets()

if __name__ == '__main__':
    root = Tk()
    w = 1150
    h = 650
    geometry = '%dx%d+%d+%d' % (w, h, 50, 0)
    root.geometry("500x300+320+200")
    root.title("Login Form")
    application = user(root)
    root.mainloop()
