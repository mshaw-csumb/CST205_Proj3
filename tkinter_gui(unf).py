__author__ = 'Bjon'

#!/usr/bin/python

import Tkinter
import tkMessageBox
from Tkinter import *

def urMumCallBack():
    tkMessageBox.showinfo( "ur mom", "is a mom")

def urDadCallBack():
    tkMessageBox.showinfo( "ur mom", "is a mom")

top = Tk()

L3 = Tkinter.Button(top,text = "Scrape me!", command = urDadCallBack)
L3.pack(side = LEFT, padx=5, pady=5)

L1 = Label(top, text="Enter name of movie or tv show:")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)

E1.pack(side = LEFT)

L2 = Tkinter.Button(top,text = "Submit", command = urMumCallBack)
L2.pack(side = RIGHT)

top.mainloop()

